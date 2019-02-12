# -*- coding: utf-8 -*-
"""Console script for flask_scenegen."""
import sys

import click
from click.testing import CliRunner

from . import flask_scenegen


def is_debugging():
    return not (sys.gettrace() is None)


@click.command()
def main(args=None):
    """Console script for flask_scenegen."""
    click.echo("Replace this message by putting your code into "
               "flask_scenegen.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    if is_debugging():
        runner = CliRunner()
        runner.invoke(main)
    else:
        main()
