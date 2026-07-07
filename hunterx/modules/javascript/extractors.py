from __future__ import annotations


class EndpointExtractor:

    def extract(
        self,
        text: str,
    ) -> list[str]:

        ...


class URLExtractor:

    def extract(
        self,
        text: str,
    ) -> list[str]:

        ...


class SecretExtractor:

    def extract(
        self,
        text: str,
    ) -> list[str]:

        ...


class DomainExtractor:

    def extract(
        self,
        text: str,
    ) -> list[str]:

        ...