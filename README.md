<div align="center">

# 🔴 FTRIYANA

### Deep Internal Reconnaissance Framework

**155-tool sequential enumeration for authorized penetration testing**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Kali](https://img.shields.io/badge/Kali-Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)](https://kali.org)
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-4.0.0-darkred?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)]()
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-☕-yellow?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/bloodravenist)

**Built by [Ajeet Kathat](https://github.com/BLOODRAVENIST)**

> ⚠️ **For Authorized Penetration Testing Only.** AI feature is **OFF in exam mode** (OffSec/CPTS/PNPT compliance).

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tool Coverage](#-tool-coverage)
- [Installation](#-installation)
- [Usage](#-usage)
- [Modes](#-modes)
- [Output](#-output)
- [AI Integration](#-ai-integration)
- [Project Structure](#-project-structure)
- [Roadmap](#-roadmap)
- [Legal](#%EF%B8%8F-legal)
- [Author](#-author)

---

## ✨ Features

| Feature | Description |
|---|---|
| **155 Tools** | Curated network recon tools from Kali Linux, sequential execution |
| **Multi-Phase** | Discovery → Service → SMB → LDAP → Web → DNS → SNMP → Mail → DB → RDP → SSH → SSL → Misc |
| **Root-Aware** | Root-only tools skipped cleanly if not root |
| **Non-Interactive** | Prevents sudo password hangs |
| **Ctrl+C Safe** | Finishes current tool, writes report, exits |
| **Markdown Report** | Auto-generated `FTRIYANA_REPORT.md` per target |
| **Error Log** | `errors/ERROR_FIX.md` with fix suggestions |
| **AI Assist (Optional)** | DeepSeek primary, Gemini fallback — OFF in exam mode |
| **AI Shell** | Interactive `/ai <question>` during scan |
| **Resume-Friendly** | Each tool's raw output saved individually |

---

## 🛠 Tool Coverage (155 tools)

<details>
<summary><b>Click to expand full tool list</b></summary>

### Host Discovery
`nmap -sn` `nmap -T4 -F` `nmap -sS -p-` `nmap -sU` `fping` `nbtscan` `arp-scan` `netdiscover` `rustscan` `hping3` `nmap -sA` `nmap -sF` `nmap -sX` `nmap -sN`

### Service Detection
`nmap -sV` `nmap -sC` `nmap -O` `nmap -A` `whatweb` `nikto` `sslscan` `sslyze`

### SMB / NetBIOS
`smbclient` `smbmap` `enum4linux-ng` `rpcclient` `smb-os-discovery` `smb-enum-shares` `smb-enum-users` `smb-security-mode` `smb-vuln*` `smb2-security-mode` `smb2-capabilities` `smb-enum-sessions` `smb-enum-domains` `smb-enum-groups` `smb-enum-processes` `smb-enum-services` `smb-ls` `smb-system-info`

### LDAP / AD
`ldapsearch` `ldap-rootdse` `ldap-search` `msrpc-enum`

### Web Enumeration
`nikto` `gobuster` `ffuf` `feroxbuster` `dirb` `dirsearch` `wpscan` `cmseek` `nuclei` `http-enum` `http-headers` `http-methods` `http-title` `http-robots.txt` `http-webdav-scan` `http-git` `http-svn-enum` `http-vuln-cve*` `curl` `waybackurls` `gowitness`

### DNS
`dig ANY` `dig axfr` `dnsrecon` `dnsenum` `fierce` `dnsx` `subfinder` `dnstwist` `dnstracer` `theHarvester` `whois` `whois-ip`

### SNMP
`snmpwalk` `snmp-check` `onesixtyone` `snmp-brute` `snmp-info` `snmp-sysdescr`

### Mail / FTP / NFS
`smtp-user-enum` `smtp-commands` `smtp-enum-users` `smtp-open-relay` `ftp-anon` `ftp-syst` `showmount` `rpcinfo` `nfs-showmount` `nfs-ls`

### Databases
`mysql-info` `mysql-empty-password` `mysql-databases` `ms-sql-info` `ms-sql-ntlm-info` `mongodb-info` `mongodb-databases` `redis-info` `oracle-tns-version`

### RDP / VNC / SSH
`rdp-enum-encryption` `rdp-ntlm-info` `rdp-vuln-ms12-020` `vnc-info` `ssh-auth-methods` `ssh-hostkey` `ssh2-enum-algos`

### Kerberos / SSL
`krb5-enum-users` `ssl-enum-ciphers` `ssl-heartbleed` `ssl-poodle` `ssl-ccs-injection` `ssl-dh-params`

### Misc / Specialized
`irc-info` `iscsi-info` `ntp-info` `upnp-info` `sip-methods` `xmpp-info` `docker-version` `kubernetes-version` `mikrotik-routeros-version` `jdwp-info` `knx-gateway-info` `p2p-conficker` `openflow-info` `nat-pmp-info` `ipv6-node-info` `ike-version`

### OSINT
`dmitry` `urlcrazy` `reconspider` `spiderfoot`

</details>

---

## 🚀 Installation

### Prerequisites
- Kali Linux (recommended) or Debian-based distro
- Python 3.8+
- SecLists installed

    sudo apt update
    sudo apt install -y seclists nmap nikto gobuster ffuf feroxbuster dnsrecon enum4linux-ng smbclient smbmap ldap-utils snmp

### Setup

    git clone https://github.com/BLOODRAVENIST/FTRIYANA.git
    cd FTRIYANA

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

---

## 💻 Usage

### Exam Mode (AI off)

    python ftriyana.py -t 10.10.10.10 --mode exam --gap 15 --i-have-permission

### AI Mode (Authorized Internal Only)

    python ftriyana.py -t 10.10.10.10 --mode ai --gap 15 --i-have-permission

### Interactive AI Shell

    python ftriyana.py -t 1.1.1.1 --ai-shell --i-have-permission

**Authorization Code:** `FTRIYANA69`

### Command-Line Options

| Flag | Description | Default |
|---|---|---|
| `-t, --target` | Target IP or hostname | **required** |
| `--mode` | `exam` / `ai` / `fast` / `deep` | `exam` |
| `--gap` | Seconds between tools | `15` |
| `--i-have-permission` | Confirm written authorization | **required** |
| `--ai-shell` | Launch AI shell only | `false` |

---

## 🎯 Modes

| Mode | AI | Gap | Tools | Use Case |
|---|---|---|---|---|
| **`exam`** | ❌ Off | 15s | 155 | OffSec / CPTS / PNPT exams |
| **`ai`** | ✅ On | 15s | 155 | Authorized internal pentest |
| **`fast`** | ❌ Off | 5s | 25 | Quick recon |
| **`deep`** | ❌ Off | 30s | 155 | Full deep enumeration |

---

## 📁 Output

    results/<target>_<timestamp>/
    ├── FTRIYANA_REPORT.md      # Markdown report
    └── raw/
        ├── nmap_ping_sweep.txt
        ├── nmap_full_tcp.txt
        ├── enum4linux_ng.txt
        ├── nikto.txt
        └── ... (155 files)

Errors → `errors/ERROR_FIX.md` with fix suggestions.

---

## 🤖 AI Integration

Edit `config/ai_config.json`:

    {
      "gemini": {
        "api_key": "",
        "model": "gemini-1.5-flash",
        "enabled": false
      },
      "deepseek": {
        "api_key": "sk-YOUR-KEY-HERE",
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com",
        "enabled": true
      },
      "primary": "deepseek"
    }

**Priority:** DeepSeek (primary) → Gemini (fallback)

> 🔒 **NEVER commit real API keys.** `config/ai_config.json` is in `.gitignore`.

---

## 📂 Project Structure

    FTRIYANA/
    ├── ftriyana.py              # Main entry point
    ├── requirements.txt
    ├── config/
    │   ├── tools.json           # 155 tool definitions
    │   └── ai_config.json       # AI keys (gitignored)
    ├── core/
    │   ├── ai_client.py         # DeepSeek + Gemini client
    │   └── ai_shell.py          # Interactive AI shell
    ├── results/                 # Scan output (gitignored)
    ├── errors/                  # Error log (gitignored)
    └── README.md

---

## 🗺 Roadmap

- [x] v4.0.0 — 155 tools, AI integration, red banner
- [ ] v4.1.0 — HTML dashboard report
- [ ] v4.2.0 — Resume support
- [ ] v4.3.0 — Advanced parsers
- [ ] v5.0.0 — 200+ tools, plugin architecture

---

## ⚖️ Legal

**Ftriyana is for authorized penetration testing only.**

- ✅ Only use on systems you have **written permission** to test
- ✅ Use in lab environments (HTB, THM, VulnHub, OSCP/CPTS labs)
- ❌ Do NOT use on systems you don't own or have permission for
- ❌ AI feature must be **OFF** during OffSec/CPTS/PNPT exams

The author is not responsible for misuse. Unauthorized access is illegal under CFAA (US), Computer Misuse Act (UK), IT Act (India), and similar laws worldwide.

---

## 👤 Author

**Ajeet Kathat** ([@BLOODRAVENIST](https://github.com/BLOODRAVENIST))

- 🐙 GitHub: [BLOODRAVENIST](https://github.com/BLOODRAVENIST)
- 📧 Email: ajeetkathatt@gmail.com

---

## ☕ Support This Project

If Ftriyana helped you in your labs, exams, or engagements, consider buying me a coffee!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support%20Ftriyana-yellow?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/bloodravenist)

Your support keeps this project alive and helps me add more tools and features.



---

<div align="center">

**⭐ If Ftriyana helped you, give it a star! ⭐**

Made with 🔴 by Ajeet Kathat

</div>
