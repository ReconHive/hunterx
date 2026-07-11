from __future__ import annotations

from hunterx.modules.params.common import CATEGORY_KEYWORDS


def classify(
    name: str,
) -> list[str]:

    normalized = name.lower().replace(
        "-",
        "_",
    )

    categories: list[str] = []

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in normalized:

                categories.append(
                    category,
                )

                break

    return categories or ["Uncategorized"]