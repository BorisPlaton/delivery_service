#!/usr/bin/env python3

from typer import Typer

from application.cli.controller.app.command import app as app_typer


def create_app() -> Typer:
    """
    The CLI utility for the delivery service application.
    """
    app = Typer(
        help="The CLI utility for the delivery service application.",
        no_args_is_help=True,
    )

    app.add_typer(app_typer)

    return app


if __name__ == '__main__':
    create_app()()
