"""Ftriyana Interactive AI Shell."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ai_client import ask
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

console = Console()


def run_shell():
    console.print(Panel.fit(
        "[bold red]Ftriyana AI Shell[/bold red]\n"
        "[dim]/ai <question>  |  /exit[/dim]\n"
        "[dim]AI requires API keys in config/ai_config.json (see README)[/dim]",
        border_style="red"
    ))
    while True:
        try:
            cmd = Prompt.ask("[bold magenta]ftriyana>[/bold magenta]")
        except (KeyboardInterrupt, EOFError):
            break
        if not cmd.strip():
            continue
        if cmd.strip() in ("/exit", "/quit", "exit", "quit"):
            break
        q = cmd[4:].strip() if cmd.startswith("/ai ") else cmd.strip()
        with console.status("[yellow]AI thinking...[/yellow]"):
            resp, prov = ask(q)
        console.print(Panel(resp, title=f"[magenta]AI ({prov})[/magenta]",
                            border_style="magenta", box=box.ROUNDED))
