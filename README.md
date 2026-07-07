<p align="center">

<svg width="180" height="180" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">

<defs>

<linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#00E5FF"/>
<stop offset="100%" stop-color="#0066FF"/>
</linearGradient>

<linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#00FFD5"/>
<stop offset="100%" stop-color="#00B894"/>
</linearGradient>

<filter id="shadow">
<feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#00D9FF"/>
</filter>

</defs>

<circle
cx="110"
cy="110"
r="90"
fill="#0D1117"
stroke="url(#g1)"
stroke-width="4"
/>

<circle
cx="110"
cy="110"
r="65"
fill="none"
stroke="#00E5FF"
stroke-width="2"
stroke-dasharray="6 6"
/>

<circle
cx="110"
cy="110"
r="42"
fill="none"
stroke="#00FFD5"
stroke-width="2"
/>

<path
d="M110 28
L118 98
L192 110
L118 122
L110 192
L102 122
L28 110
L102 98Z"
fill="url(#g1)"
filter="url(#shadow)"
opacity="0.95"
/>

<circle
cx="110"
cy="110"
r="8"
fill="#FFFFFF"
/>

<text
x="110"
y="212"
text-anchor="middle"
font-size="18"
font-family="Segoe UI,Arial,sans-serif"
font-weight="700"
fill="#58A6FF">
HunterX
</text>

</svg>

</p>

<h1 align="center">HunterX</h1>

<p align="center">
Modern Modular Reconnaissance Framework
<br>
Built for Bug Bounty Hunters • Pentesters • Security Researchers
</p>

---

# HunterX

HunterX is a modern reconnaissance framework written entirely in Python.

It is designed for bug bounty hunters, penetration testers and security researchers who need a fast, modular and extensible reconnaissance toolkit.

Unlike traditional monolithic scanners, HunterX uses an independent plugin architecture, allowing every module to work individually or as part of a complete reconnaissance pipeline.

---

# Features

- Modular architecture
- Plugin-based design
- Fast HTTP engine
- DNS reconnaissance
- Subdomain enumeration
- JavaScript analysis
- Web crawler
- Directory brute forcing
- Security header analysis
- Cookie analysis
- CORS analysis
- Technology fingerprinting
- Workspace support
- JSON reports
- Markdown reports
- Colored terminal UI
- Progress bars
- Rich logging
- Extensible API

---

# Installation

## Using pip

```bash
pip install hunterx-reconhive
```

## Using uv

```bash
uv tool install hunterx-reconhive
```

---

# Usage

Basic scan

```bash
hunterx scan example.com
```

Run specific plugins

```bash
hunterx scan example.com --plugins dns,http,crawler
```

Custom HTTP headers

```bash
hunterx scan example.com -H "Authorization: Bearer TOKEN"
```

POST request

```bash
hunterx scan example.com -X POST
```

Directory scan

```bash
hunterx scan example.com --plugins directory
```

Crawler

```bash
hunterx scan example.com --plugins crawler
```

JavaScript analysis

```bash
hunterx scan example.com --plugins javascript
```

Generate JSON report

```bash
hunterx scan example.com -o report.json
```

Generate Markdown report

```bash
hunterx scan example.com -o report.md
```

---

# Available Plugins

| Plugin | Description |
|---------|-------------|
| dns | DNS Reconnaissance |
| http | HTTP Analysis |
| crawler | Website Crawling |
| javascript | JavaScript Analysis |
| directory | Directory Enumeration |
| subdomain | Subdomain Enumeration |
| tls | TLS Scanner |
| ports | Port Scanner |

---

# Example

```bash
hunterx scan google.com --plugins dns,http,crawler,javascript -o report.json
```

---

# Project Structure

```
hunterx/
│
├── cli/
├── core/
├── modules/
├── plugins/
└── utils/
```

---

# Architecture

```
CLI

↓

Core Engine

↓

Plugin Loader

↓

Plugins

↓

Modules

↓

Result Objects

↓

Workspace / Report
```

---

# Current Modules

✅ DNS

✅ HTTP

✅ Cookies

✅ Security Headers

✅ CORS

✅ Fingerprinting

✅ Directory Scanner

✅ Web Crawler

✅ JavaScript Analyzer

---

# Roadmap

-

- TLS Scanner improvements
- Port Scanner
- WAF Detection
- Screenshot Engine
- Parameter Discovery
- Archive.org integration
- Wayback Machine
- CDN Detection
- ASN Lookup
- CSP Analyzer
- HTTP/2 & HTTP/3 analysis
- HTTP Request Smuggling checks
- GraphQL discovery
- Swagger/OpenAPI detection
- Secret Discovery
- AWS bucket discovery
- Passive Recon
- Shodan integration
- Censys integration
- VirusTotal integration
- HTML Report
- Live Dashboard

---

# Why HunterX?

HunterX focuses on

- Clean architecture
- High performance
- Readable output
- Easy plugin development
- Modern Python practices
- Lightweight dependencies

---

# Contributing

Contributions are welcome.

Fork the repository

Create your feature branch

Submit a Pull Request

---

# License

MIT License

---

# Disclaimer

HunterX is intended for educational purposes and authorized security assessments only.

The author is not responsible for any misuse.
