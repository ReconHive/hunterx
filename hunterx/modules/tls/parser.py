from __future__ import annotations

from datetime import datetime
from datetime import timezone


class CertificateParser:

    def parse(
        self,
        cert: dict,
    ) -> dict:

        issuer = dict(
            x[0]
            for x in cert.get(
                "issuer",
                [],
            )
        )

        subject = dict(
            x[0]
            for x in cert.get(
                "subject",
                [],
            )
        )

        san = [

            value

            for key, value in cert.get(
                "subjectAltName",
                [],
            )

            if key == "DNS"

        ]

        expires_raw = cert.get(
            "notAfter",
        )

        expires = None

        days = None

        expired = False

        if expires_raw:

            dt = datetime.strptime(

                expires_raw,

                "%b %d %H:%M:%S %Y %Z",

            )

            expires = dt.isoformat()

            delta = dt.replace(
                tzinfo=timezone.utc,
            ) - datetime.now(
                timezone.utc,
            )

            days = delta.days

            expired = days < 0

        issuer_cn = issuer.get(
            "commonName",
        )

        subject_cn = subject.get(
            "commonName",
        )

        wildcard = any(

            name.startswith("*.")

            for name in san

        )

        return {

            "issuer": issuer_cn,

            "subject": subject_cn,

            "san": san,

            "expires": expires,

            "days_remaining": days,

            "expired": expired,

            "self_signed": issuer_cn == subject_cn,

            "wildcard": wildcard,

            "serial": cert.get(
                "serialNumber",
            ),

            "signature_algorithm": cert.get(
                "signatureAlgorithm",
            ),

        }