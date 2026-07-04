from __future__ import annotations

from urllib.parse import urljoin
from urllib.parse import urlparse


class URLNormalizer:

    def normalize(
        self,
        base: str,
        url: str,
    ) -> str:

        return urljoin(
            base,
            url,
        )

    def same_origin(
        self,
        base: str,
        url: str,
    ) -> bool:

        return (
            urlparse(base).netloc
            ==
            urlparse(url).netloc
        )