<p align="center">
  <img src="docs/logo.png" width="180">
</p>

<h1 align="center">
HunterX
</h1>

<p align="center">

Modern Modular Reconnaissance Framework for Bug Bounty Hunters & Security Researchers

</p>

<p align="center">

Python • Fast • Modular • Extensible

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
hunterx scan example.com \
    --plugins dns,http,crawler
```

Custom HTTP headers

```bash
hunterx scan example.com \
    -H "Authorization: Bearer TOKEN"
```

POST request

```bash
hunterx scan example.com \
    -X POST
```

Directory scan

```bash
hunterx scan example.com \
    --plugins directory
```

Crawler

```bash
hunterx scan example.com \
    --plugins crawler
```

JavaScript analysis

```bash
hunterx scan example.com \
    --plugins javascript
```

Generate JSON report

```bash
hunterx scan example.com \
    -o report.json
```

Generate Markdown report

```bash
hunterx scan example.com \
    -o report.md
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
hunterx scan google.com \
    --plugins dns,http,crawler,javascript \
    -o report.json
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
