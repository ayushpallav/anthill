"""
Core scripts to handle cli instructions
"""

import sys
import click
import yaml
import json
import pathlib

from .management import Nest
from anthill import __version__


@click.group()
def main():
    """
    Orchastrate. Build. Run.
    """
    pass


@main.command()
def version():
    click.echo("Version: " + __version__)

@main.command()
@click.argument('nest', type=click.File('r'))
@click.option('--run', '-r', is_flag=True, help="Run the anthill after build")
def build(nest, run):
    """
    Build anthill using the yml file provided
    """
    _dir = pathlib.Path(nest.name).absolute().parent
    _nest = json.dumps(yaml.safe_load(nest))
    nest_obj  = Nest(nest=_nest, _dir=_dir)
    try:
        nest_obj.build()
    except Exception as err:
        click.echo(f"Aborting build ... \n {err.message}")
    else:
        click.echo("Anthill built successfully !")
        if run:
            try:
                nest_obj.run()
            except Exception as err:
                click.echo(f"Aborting execution ... \n {err.message}")
            else:
                click.echo("Anthill initiated successfully !")
    return 0
