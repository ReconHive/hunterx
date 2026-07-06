from __future__ import annotations

SERVICES  = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    111: "rpcbind",
    135: "msrpc",
    139: "netbios",
    143: "imap",
    389: "ldap",
    443: "https",
    445: "smb",
    465: "smtps",
    587: "smtp",
    993: "imaps",
    995: "pop3s",
    1433: "mssql",
    1521: "oracle",
    2049: "nfs",
    2375: "docker",
    3306: "mysql",
    3389: "rdp",
    5432: "postgres",
    5900: "vnc",
    5985: "winrm",
    6379: "redis",
    8080: "http-alt",
    8443: "https-alt",
    9000: "php-fpm",
    9200: "elasticsearch",
    11211: "memcached",
    27017: "mongodb",
}


def detect_service(port: int) -> str:
    return SERVICES.get(
        port,
        "unknown",
    )