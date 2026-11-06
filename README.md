<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=38&duration=2500&pause=800&color=9F4FFF&center=true&vCenter=true&multiline=true&width=900&height=120&lines=%F0%9F%A4%96+FTRIYANA;AI-Powered+Pentesting;70%2B+Tools+%2B+AI+Shell;Recon.+Analyze.+Exploit." alt="Typing SVG" />

# FTRIYANA

### AI-Powered Penetration Testing Framework

**70+ pentesting tools orchestrated by an AI shell that thinks, plans, and executes**

**Made by [BLOODRAVENIST](https://github.com/BLOODRAVENIST)**

> **For Authorized Bug Bounty & Penetration Testing Only**

---

## What Is FTRIYANA?

**FTRIYANA** is an **AI-driven pentesting framework** that combines 70+ security tools (nmap, nuclei, wpscan, smbmap, feroxbuster, etc.) with an **AI client** that plans attacks, analyzes results, and suggests next steps. It's recon on autopilot.

**Why FTRIYANA?**

- **AI Shell** - `ai_shell.py` interprets results and suggests next moves
- **70+ Tools** - nmap, nuclei, wpscan, smbmap, feroxbuster, gobuster, ffuf, nikto, enum4linux, rustscan
- **Smart Planning** - AI reads output and chains tools automatically
- **Structured Results** - `results/TARGET_TIMESTAMP/raw/` + `reports.json`
- **Modular Core** - `core/ai_client.py`, `core/ai_shell.py`

---

## Features

| Feature | Description |
|---|---|
| **AI Shell** | LLM-powered analysis of tool output |
| **70+ Tools** | nmap, nuclei, wpscan, smbmap, rpcclient, enum4linux-ng, rustscan, ffuf, gobuster, feroxbuster, nikto, subfinder, theharvester, dirb, dirsearch, dnsenum, dnsrecon, dnstwist, whatweb, cmseek |
| **AI Config** | `config/ai_config.json` — plug in your LLM API key |
| **JSON Reports** | `reports.json` + `Result/TARGET/cms.json` |
| **Structured Raw** | Every tool's output saved per-scan |
| **CMS Detection** | cmseek + whatweb integrated |

---

## Tools Integrated

### Recon
`subfinder`, `theharvester`, `dnsenum`, `dnsrecon`, `dnstracer`, `dnstwist`, `dnsx`, `dig_any`, `dig_axfr`

### Scanning
`nmap_fast`, `nmap_default_scripts`, `nmap_service_version`, `rustscan`, `fping_sweep`, `nmap_ping_sweep`

### Web
`nikto`, `whatweb`, `cmseek`, `wpscan`, `nuclei_safe`, `ffuf_dir`, `gobuster_dir`, `dirb`, `dirsearch`, `feroxbuster`, `curl_headers`, `curl_robots`, `curl_sitemap`

### SMB / Windows
`enum4linux_ng`, `smbclient_list`, `smbmap`, `rpcclient_enumdomusers`, `nbtscan`, `nmap_smb_*` (12+ scripts)

### LDAP / HTTP
`ldapsearch_anon`, `nmap_ldap_*`, `nmap_http_*` (10+ scripts)

### Screenshots
`gowitness`

---

## Architecture
ftriyana.py (main)
|
+-- core/
| +-- ai_client.py # LLM API client
| +-- ai_shell.py # interactive AI shell
|
+-- config/
| +-- ai_config.json # API keys, model
| +-- tools.json # tool registry
|
+-- results/TARGET_TIMESTAMP/
| +-- raw/ # per-tool output
+-- Result/TARGET/
+-- cms.json # CMS detection

text

---

## Installation

### Prerequisites

- Kali Linux
- Python 3.10+
- 70+ tools (nmap, nuclei, wpscan, etc.)
- LLM API key (OpenAI / Anthropic / local)

### Clone & Setup

```bash
git clone https://github.com/BLOODRAVENIST/FTRIYANA.git
cd FTRIYANA
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Configure AI
bash
nano config/ai_config.json
# Add your API key
Run
bash
python3 ftriyana.py 127.0.0.1
Usage
bash
# Basic scan
python3 ftriyana.py target.com

# Interactive AI shell
python3 ftriyana.py target.com --ai

# Check results
cat results/target_TIMESTAMP/reports.json
Output:

text
results/target_TIMESTAMP/
├── raw/
│   ├── nmap_fast.txt
│   ├── nuclei_safe.txt
│   ├── wpscan.txt
│   ├── smbmap.txt
│   └── ... (70+ files)
reports.json
Result/target/cms.json
File Structure
text
FTRIYANA/
├── core/
│   ├── ai_client.py
│   └── ai_shell.py
├── config/
│   ├── ai_config.json
│   └── tools.json
├── errors/
│   └── ERROR_FIX.md
├── Result/TARGET/cms.json
├── results/TARGET_TIMESTAMP/raw/
├── ftriyana.py
├── reports.json
├── requirements.txt
├── LICENSE
└── README.md
Troubleshooting
Issue	Fix
ModuleNotFoundError	source venv/bin/activate && pip install -r requirements.txt
AI not responding	Check config/ai_config.json API key
Tool missing	which nmap — install missing tools
Empty reports	Check results/*/raw/ for per-tool errors
Legal
FTRIYANA is for authorized bug bounty and penetration testing only.

Only use on targets within valid bug bounty scope

Use for authorized pentesting with written permission

Use in lab environments (HTB, THM, VulnHub)

Do NOT use on systems you do not own

Unauthorized access is illegal under CFAA (US), Computer Misuse Act (UK), IT Act (India), and similar laws worldwide.

Support
If FTRIYANA helped you, consider buying me a coffee!

https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support%20FTRIYANA-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black

<div align="center">
Made by BLOODRAVENIST
If FTRIYANA helped you, give it a star!

BLOODRAVENIST | FTRIYANA

<img src="https://capsule-render.vercel.app/api?type=waving&color=9F4FFF&height=100&section=footer&text=AI%20Recon&fontSize=32&fontColor=ffffff&animation=twinkling" width="100%"/>

</div>
