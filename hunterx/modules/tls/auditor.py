from __future__ import annotations


class TLSAuditor:

    def audit(
        self,
        result: dict,
    ) -> list[str]:

        findings: list[str] = []

        if result["expired"]:

            findings.append(
                "Expired Certificate",
            )

        if result["self_signed"]:

            findings.append(
                "Self Signed Certificate",
            )

        if result["wildcard"]:

            findings.append(
                "Wildcard Certificate",
            )

        if (

            result["days_remaining"] is not None

            and

            result["days_remaining"] < 30

        ):

            findings.append(
                "Certificate expires soon",
            )

        return findings