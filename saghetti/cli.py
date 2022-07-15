import time

import rich
import typer
from rich.panel import Panel

from .animation import frames


def main():
    console = rich.console.Console()

    for frame in frames:
        console.clear()

        console.print(
            Panel(
                (
                    f"{frame}\n\n"
                    "[green]Eat the saghetti to forgetti the regretti![/]\n\n"
                    "Become a [bold]EuroPython[/] volunteer!\n\n"
                    "Email us at [bold underline]volunteers@europython.eu"
                ),
                border_style="blue",
            )
        )
        time.sleep(0.125)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    typer.run(main)
