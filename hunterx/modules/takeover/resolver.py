from __future__ import annotations

import dns.resolver

from hunterx.core.context import ScanContext


class CNAMEResolver:
    """
    Follow a host's CNAME chain to its terminus.
    """

    MAX_DEPTH = 10

    def resolve_chain(
        self,
        context: ScanContext,
        host: str,
    ) -> tuple[list[str], bool]:
        """
        Returns (chain, dangling).

        chain: CNAME targets in order (host itself not included).
        dangling: True if the chain's end is unresolvable
                  (NXDOMAIN) - the core takeover signal.
        """

        chain: list[str] = []

        current = host

        seen: set[str] = {host}

        dangling = False

        for _ in range(self.MAX_DEPTH):

            try:

                answers = context.dns.resolver.resolve(
                    current,
                    "CNAME",
                )

            except dns.resolver.NXDOMAIN:

                dangling = True

                break

            except Exception:

                #
                # NoAnswer (no CNAME at this name) or a
                # resolver-level error - chain ends here,
                # not a dangling signal on its own.
                #

                break

            target = str(
                answers[0].target,
            ).rstrip(".")

            if target in seen:

                #
                # CNAME loop - bail, nothing actionable.
                #

                break

            seen.add(target)

            chain.append(target)

            current = target

        if not dangling and chain:

            try:

                context.dns.resolver.resolve(
                    current,
                    "A",
                )

            except dns.resolver.NXDOMAIN:

                dangling = True

            except Exception:

                pass

        return chain, dangling