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

FETCH = re.compile(
    r'fetch\(\s*["\']([^"\']+)["\']'
)

AXIOS = re.compile(
    r'axios\.(?:get|post|put|delete|patch)\(\s*["\']([^"\']+)["\']'
)

XHR = re.compile(
    r'open\(\s*["\'][A-Z]+["\']\s*,\s*["\']([^"\']+)["\']'
)

WEBSOCKET = re.compile(
    r'wss?://[^\s"\']+'
)

GRAPHQL = re.compile(
    r'["\']([^"\']*graphql[^"\']*)["\']',
    re.I,
)

FIREBASE = re.compile(
    r'firebaseio\.com'
)

GOOGLE_CLIENT = re.compile(
    r'[0-9]{12}-[A-Za-z0-9]{32}\.apps\.googleusercontent\.com'
)

STRIPE = re.compile(
    r'pk_live_[A-Za-z0-9]{24,}'
)

S3 = re.compile(
    r'[A-Za-z0-9.\-]+\.s3\.amazonaws\.com'
)

CLOUDFRONT = re.compile(
    r'[A-Za-z0-9.\-]+\.cloudfront\.net'
)

AZURE = re.compile(
    r'https://[A-Za-z0-9\-]+\.blob\.core\.windows\.net'
)

BEARER = re.compile(
    r'Bearer\s+[A-Za-z0-9._\-]+'
)

GITHUB = re.compile(
    r'gh[pousr]_[A-Za-z0-9]{36,}'
)

API_KEY = re.compile(
    r'(?i)(?:api[_-]?key|apikey)["\']?\s*[:=]\s*["\']([A-Za-z0-9_\-]{16,})'
)

BASE_URL = re.compile(
    r'https?://[A-Za-z0-9./:_\-]+'
)


