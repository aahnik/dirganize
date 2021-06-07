"""Command line interface for dirganize."""

import logging
import os
from typing import Optional

import typer
from rich.logging import RichHandler

from dirganize import __version__
from dirganize.dirganize import dirganize

app = typer.Typer(add_completion=False)


def version_callback(value: bool):
    """Show current version and exit."""
    if value:
        print(__version__)
        raise typer.Exit()


def verbosity_callback(value: bool):
    """Set logging level."""
    if value:
        logging.basicConfig(
            level=logging.INFO,
            format="[dim]%(name)s[/dim]\t%(message)s",
            handlers=[
                RichHandler(
                    markup=True,
                    show_path=False,
                )
            ],
        )
        logging.info("Loud logging enabled.")


@app.command()
def main(
    path: str = typer.Option(
        os.getcwd(),
        "--path",
        "-p",
        help="Path of the directory to dirganize",
    ),
    verbose: Optional[bool] = typer.Option(  # pylint: disable=unused-argument
        None,
        "--loud",
        "-l",
        callback=verbosity_callback,
        envvar="LOUD",
        help="Increase output verbosity.",
    ),
    version: Optional[bool] = typer.Option(  # pylint: disable=unused-argument
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Show version and exit.",
    ),
):
    """Declutter you folders and get peace of mind.

    A command-line tool to organize files into category directories.
    """
    dirganize(path=path)
