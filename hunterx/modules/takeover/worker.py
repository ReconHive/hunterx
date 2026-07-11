from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.takeover.fingerprints import TakeoverFingerprint
from hunterx.modules.takeover.fingerprints import match
from hunterx.modules.takeover.resolver import CNAMEResolver


class TakeoverWorker:

    def __init__(self) -> None:

        self.resolver = CNAMEResolver()

    def check(
        self,
        context: ScanContext,
        host: str,
    ) -> dict | None:

        chain, dangling = self.resolver.resolve_chain(
            context,
            host,
        )

        if not chain:
            return None

        final = chain[-1]

        fingerprint = match(final)

        if fingerprint is None:
            return None

        #
        # nxdomain_only services (Azure, Elastic Beanstalk,
        # Discourse, ...): the ONLY valid signal is dangling DNS.
        # A live host check doesn't apply - there's nothing to
        # fetch if the whole point is that it doesn't resolve.
        #

        if fingerprint.nxdomain_only:

            if not dangling:
                return None

            return self._build_finding(
                host=host,
                fingerprint=fingerprint,
                chain=chain,
                dangling=True,
                matched_via="nxdomain",
            )

        #
        # Already dangling via generic A-record check (from
        # resolve_chain) - confirmed regardless of fingerprint
        # signature/status, since there's nothing live to verify
        # against anyway.
        #

        if dangling:

            return self._build_finding(
                host=host,
                fingerprint=fingerprint,
                chain=chain,
                dangling=True,
                matched_via="nxdomain",
            )

        #
        # CNAME resolves and points to a fingerprinted service,
        # but isn't dangling at the DNS level - fetch the host
        # and check the body signature and/or expected status.
        #

        response = None

        for scheme in (
            "https",
            "http",
        ):

            try:

                response = context.http.get(
                    f"{scheme}://{host}",
                )

                break

            except Exception:

                continue

        if response is None:
            return None

        signature_hit = (
            fingerprint.signature is not None
            and fingerprint.signature.lower()
            in response.text.lower()
        )

        status_hit = (
            fingerprint.expected_status is not None
            and response.status_code
            == fingerprint.expected_status
        )

        if not signature_hit and not status_hit:
            return None

        if signature_hit and status_hit:

            matched_via = "signature+status"

        elif signature_hit:

            matched_via = "signature"

        else:

            matched_via = "status"

        return self._build_finding(
            host=host,
            fingerprint=fingerprint,
            chain=chain,
            dangling=False,
            matched_via=matched_via,
        )

    def _build_finding(
        self,
        host: str,
        fingerprint: TakeoverFingerprint,
        chain: list[str],
        dangling: bool,
        matched_via: str,
    ) -> dict:

        #
        # Effective confidence: even a "high" confidence
        # fingerprint drops to "medium" if the only match was
        # a bare HTTP status code, since status-only matches are
        # inherently weaker evidence than a body signature or a
        # confirmed dangling DNS record.
        #

        confidence = fingerprint.confidence

        if matched_via == "status" and confidence == "high":

            confidence = "medium"

        return {
            "host": host,
            "service": fingerprint.service,
            "cname": chain[-1],
            "chain": chain,
            "dangling_dns": dangling,
            "matched_via": matched_via,
            "confidence": confidence,
        }