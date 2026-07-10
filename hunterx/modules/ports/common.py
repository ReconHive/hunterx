from __future__ import annotations

DEFAULT_PORTS = [
    20,
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    111,
    135,
    139,
    143,
    389,
    443,
    445,
    465,
    587,
    993,
    995,
    1433,
    1521,
    2049,
    2375,
    3306,
    3389,
    5432,
    5900,
    5985,
    6379,
    8080,
    8443,
    9000,
    9200,
    11211,
    27017,
]


def parse_ports(
    spec: str,
) -> list[int]:
    """
    Parse a port specification string into a sorted list of ports.

    Supports:
        "22"            -> [22]
        "22,25,1000"    -> [22, 25, 1000]
        "1-1000"        -> [1, 2, ..., 1000]
        "22,100-200"    -> mixed
        "-" or "all"    -> full 1-65535 range

    Raises ValueError on malformed input.
    """

    spec = spec.strip().lower()

    if spec in (
        "-",
        "all",
    ):

        return list(
            range(1, 65536)
        )

    ports: set[int] = set()

    for part in spec.split(","):

        part = part.strip()

        if not part:
            continue

        if "-" in part:

            start_str, end_str = part.split(
                "-",
                1,
            )

            start = int(start_str.strip())

            end = int(end_str.strip())

            if start > end:

                start, end = end, start

            ports.update(
                range(start, end + 1)
            )

        else:

            ports.add(
                int(part)
            )

    return sorted(
        port
        for port in ports
        if 1 <= port <= 65535
    )