from __future__ import annotations

#
# category -> keyword substrings matched against normalized
# (lowercase, dash->underscore) parameter names.
#

CATEGORY_KEYWORDS: dict[str, list[str]] = {

    "IDOR / Access Control": [
        "id",
        "uid",
        "user_id",
        "userid",
        "account",
        "account_id",
        "profile_id",
        "order_id",
        "invoice_id",
        "customer_id",
        "ref",
        "reference",
        "owner",
    ],

    "Open Redirect": [
        "redirect",
        "redirect_uri",
        "redirect_url",
        "return",
        "return_to",
        "returnurl",
        "next",
        "dest",
        "destination",
        "continue",
        "target",
        "out",
        "forward",
        "goto",
    ],

    "SSRF": [
        "url",
        "uri",
        "dest",
        "target",
        "proxy",
        "fetch",
        "host",
        "domain",
        "feed",
        "src",
        "endpoint",
        "callback_url",
    ],

    "LFI / Path Traversal": [
        "file",
        "path",
        "filename",
        "filepath",
        "folder",
        "dir",
        "document",
        "template",
        "page",
        "load",
        "include",
    ],

    "Command Injection": [
        "cmd",
        "exec",
        "command",
        "run",
        "execute",
        "shell",
        "ping",
    ],

    "SQL Injection Candidate": [
        "id",
        "search",
        "query",
        "filter",
        "sort",
        "order",
        "category",
        "q",
    ],

    "JSONP / Callback Injection": [
        "callback",
        "jsonp",
        "cb",
    ],

    "Debug / Hidden Functionality": [
        "debug",
        "test",
        "admin",
        "dev",
        "staging",
        "beta",
        "internal",
        "hidden",
        "bypass",
    ],

    "Authentication / Token": [
        "token",
        "auth",
        "apikey",
        "api_key",
        "access_token",
        "session",
        "sessionid",
        "jwt",
        "secret",
        "key",
    ],

}


#
# Categories worth surfacing prominently - direct exploitation
# potential, not just "interesting to look at."
#

HIGH_RISK_CATEGORIES = {
    "IDOR / Access Control",
    "Open Redirect",
    "SSRF",
    "LFI / Path Traversal",
    "Command Injection",
    "SQL Injection Candidate",
}