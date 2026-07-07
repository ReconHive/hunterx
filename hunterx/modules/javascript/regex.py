from __future__ import annotations

import re

URL = re.compile(
    r"https?://[^\s\"'<>]+",
)

ENDPOINT = re.compile(
    r"(?<![A-Za-z0-9])/(?:[A-Za-z0-9_\-./]+)",
)

DOMAIN = re.compile(
    r"(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}",
)

JWT = re.compile(
    r"eyJ[A-Za-z0-9_\-=]+\.[A-Za-z0-9_\-=]+\.[A-Za-z0-9_\-=]+",
)

GOOGLE_API = re.compile(
    r"AIza[0-9A-Za-z\-_]{35}",
)

AWS_ACCESS_KEY = re.compile(
    r"AKIA[0-9A-Z]{16}",
)

SLACK_TOKEN = re.compile(
    r"xox[baprs]-[A-Za-z0-9-]+",
)

PRIVATE_KEY = re.compile(
    r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----",
)