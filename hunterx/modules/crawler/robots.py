from __future__ import annotations

class RobotsParser:

    def parse(
        self,
        text: str,
    ) -> list[str]:

        paths: list[str] = []

        for line in text.splitlines():

            line = line.strip()

            if (
                line.startswith("Allow:")
                or line.startswith("Disallow:")
            ):

                value = line.split(
                    ":",
                    1,
                )[1].strip()

                if value:

                    paths.append(value)

        return sorted(
            set(paths)
        )