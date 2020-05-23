"""
Core scripts to handle cli instructions
"""

import sys
import click
import yaml
import json

from .management import Nest


@click.group()
def main():
    """
    Orchastrate. Build. Run.
    """
    pass


@main.command()
@click.argument('nest', type=click.File('r'))
@click.option('--run', '-r', is_flag=True, help="Run the anthill after build")
def build(nest, run):
    """
    Build anthill using the yml file provided
    """
    click.echo("Ants building your anthill, hold tight !")
    _nest = json.dumps(yaml.safe_load(nest))
    nest_obj  = Nest(nest=_nest)
    nest_obj.build()
    click.echo("Anthill built successfully !")
    if run:
        nest_obj.run()
    return 0
