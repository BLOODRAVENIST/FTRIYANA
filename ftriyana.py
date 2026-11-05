#!/usr/bin/env python3
"""Ftriyana v4.0.0 — Deep Internal Reconnaissance Framework
by BLOODRAVENIST · For Authorized Testing Only"""
import os, sys, json, time, hashlib, argparse, subprocess, signal
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import pyfiglet

VERSION = "4.0.0"
SECRET_HASH = hashlib.sha256(b"FTRIYANA69").hexdigest()
BASE = Path(__file__).parent
CFG = BASE / "config"
OUT = BASE / "results"
ERR = BASE / "errors"
sys.path.insert(0, str(BASE / "core"))

console = Console()


def banner():
    console.print(f"[bold red]{pyfiglet.figlet_format('FTRIYANA', font='ansi_shadow')}[/bold red]")
    console.print(Panel.fit(
        "[bold red]DEEP INTERNAL RECONNAISSANCE FRAMEWORK[/bold red]\n"
        "[dim red]by BLOODRAVENIST · For Authorized Testing Only[/dim red]\n"
        f"[dim red]v{VERSION}[/dim red]",
        border_style="red", box=box.DOUBLE))


def auth():
    console.print("\n[bold red]⚠  Authorization Required[/bold red]")
    for i in range(3, 0, -1):
        try:
            code = Prompt.ask("[red]Enter Authorization Code[/red]", password=True)
        except (KeyboardInterrupt, EOFError):
            sys.exit(1)
        if hashlib.sha256(code.encode()).hexdigest() == SECRET_HASH:
            console.print("[bold green]✓ Authorized.[/bold green]\n")
            return
        console.print(f"[red]✗ Invalid. {i-1} left.[/red]")
    sys.exit(1)


def check_target(target):
    try:
        r = subprocess.run(["ping", "-c", "1", "-W", "2", target],
                           capture_output=True, timeout=5)
        return r.returncode == 0
    except Exception:
        return False


def run_tool(tool, target, outdir, timeout, is_root):
    if tool.get("root") and not is_root:
        return False, "SKIPPED (needs root)"
    cmd = tool["command"].replace("<target>", target).replace("<domain>", target)
    outfile = outdir / "raw" / f"{tool['name']}.txt"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    full_cmd = f"timeout {timeout}s bash -c {json.dumps(cmd)} </dev/null 2>&1"
    try:
        with open(outfile, "w") as f:
            f.write(f"# {tool['name']}\n# cmd: {cmd}\n# time: {datetime.now().isoformat()}\n")
            f.write("# " + "=" * 60 + "\n\n")
            r = subprocess.run(full_cmd, shell=True, capture_output=True,
                               text=True, timeout=timeout + 15)
            f.write(r.stdout or "")
            if r.stderr:
                f.write("\n# STDERR:\n" + r.stderr)
        if r.returncode == 0:
            return True, ""
        if r.returncode == 124:
            return False, f"Timeout {timeout}s"
        return False, f"Exit {r.returncode}"
    except subprocess.TimeoutExpired:
        return False, f"Hard timeout {timeout}s"
    except Exception as e:
        return False, str(e)


def log_error(tool, reason):
    ERR.mkdir(exist_ok=True)
    f = ERR / "ERROR_FIX.md"
    first = not f.exists()
    with open(f, "a") as fh:
        if first:
            fh.write("# Ftriyana — Error Log\n\n")
        fh.write(f"## {tool}\n- **Reason:** {reason}\n- **Time:** {datetime.now().isoformat()}\n")
        fh.write(f"- **Fix:** check `which {tool.split('_')[0]}`\n\n")


def write_report(outdir, target, results, elapsed):
    total = len(results)
    ok = sum(1 for r in results if r["ok"])
    rep = outdir / "FTRIYANA_REPORT.md"
    with open(rep, "w") as f:
        f.write("# Ftriyana Recon Report\n\n")
        f.write(f"**Target:** `{target}`  \n**Time:** {datetime.now().isoformat()}  \n")
        f.write(f"**Elapsed:** {elapsed:.1f}s  \n**Tools:** {ok}/{total} succeeded  \n\n")
        f.write("## Results\n\n| # | Tool | Status | Reason |\n|---|---|---|---|\n")
        for i, r in enumerate(results, 1):
            status = "OK" if r["ok"] else "FAIL"
            f.write(f"| {i} | {r['tool']} | {status} | {r['reason'] or '-'} |\n")
        f.write("\n## Raw outputs: `raw/`\n")
    return rep


def main():
    p = argparse.ArgumentParser(description="Ftriyana v4")
    p.add_argument("-t", "--target", required=True)
    p.add_argument("--mode", choices=["exam", "ai", "fast", "deep"], default="exam")
    p.add_argument("--gap", type=int, default=15)
    p.add_argument("--i-have-permission", action="store_true", required=True)
    p.add_argument("--ai-shell", action="store_true")
    args = p.parse_args()

    banner()
    if args.ai_shell:
        from ai_shell import run_shell
        run_shell()
        return

    auth()

    if args.mode == "ai":
        console.print("[yellow]⚠ AI MODE — Not for OffSec/CPTS/PNPT exams.[/yellow]\n")
    else:
        console.print("[dim]Exam mode: AI off.[/dim]\n")

    tools = json.load(open(CFG / "tools.json"))
    if args.mode == "fast":
        tools = tools[:25]

    console.print("[red]Pre-flight...[/red]")
    is_root = os.geteuid() == 0
    if not check_target(args.target):
        console.print(f"[red]✗ Target {args.target} unreachable[/red]")
        sys.exit(1)

    available, skipped = [], []
    for t in tools:
        bin_name = t["command"].split()[0]
        if t.get("root") and not is_root:
            skipped.append((t["name"], "needs root"))
            continue
        if subprocess.run(["which", bin_name], capture_output=True).returncode != 0:
            skipped.append((t["name"], "not installed"))
            continue
        available.append(t)

    tbl = Table(show_header=False, box=box.SIMPLE)
    tbl.add_column("Check", style="red")
    tbl.add_column("Status")
    tbl.add_row("Root", "✓" if is_root else "⚠ not root")
    tbl.add_row("Target", f"✓ {args.target}")
    tbl.add_row("Tools", f"✓ {len(available)}/{len(tools)}")
    if skipped:
        tbl.add_row("Skipped", f"⚠ {len(skipped)}")
    console.print(tbl)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = OUT / f"{args.target}_{ts}"
    outdir.mkdir(parents=True, exist_ok=True)

    interrupted = [False]
    def sigint(sig, frame):
        interrupted[0] = True
        console.print("\n[yellow]Interrupted — finishing current tool...[/yellow]")
    signal.signal(signal.SIGINT, sigint)

    console.print(f"\n[bold red]Starting: {len(available)} tools · gap {args.gap}s[/bold red]\n")
    start = time.time()
    results = []

    for idx, tool in enumerate(available, 1):
        if interrupted[0]:
            console.print("[yellow]Stopping...[/yellow]")
            break
        console.print(f"[red][{idx}/{len(available)}][/red] {tool['name']}", end=" ")
        ok, reason = run_tool(tool, args.target, outdir, tool.get("timeout", 300), is_root)
        results.append({"tool": tool["name"], "ok": ok, "reason": reason})
        if ok:
            console.print("[green]✓[/green]")
        else:
            console.print(f"[red]✗ {reason}[/red]")
            log_error(tool["name"], reason)
        if idx < len(available) and not interrupted[0]:
            time.sleep(args.gap)

    elapsed = time.time() - start
    report = write_report(outdir, args.target, results, elapsed)

    console.print("\n" + "=" * 60)
    ok_count = sum(1 for r in results if r["ok"])
    console.print(Panel.fit(
        f"[bold green]Complete[/bold green]\n"
        f"Tools: {ok_count}/{len(results)}  ·  Time: {elapsed:.1f}s\n"
        f"Report: [red]{report}[/red]\nOutput: {outdir}",
        border_style="red"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Done.[/yellow]")
        sys.exit(130)
