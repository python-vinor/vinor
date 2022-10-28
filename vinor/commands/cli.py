import json
import os
import click
from .utils import (
    camel_to_snake
)
from .initializer import Initializer


def process_common_name(ctx, param, value):
    output = ''
    if value is not None:
        output = camel_to_snake(value).lower()
    return output


@click.group()
def cli():
    pass


@click.group()
def generate():
    pass


@cli.command()
def init():
    """
    Initialize as vinor project
        - vinor init
    """
    project_root = os.getcwd()
    initializer = Initializer(project_root)
    initializer.write_config()
    click.echo('Created configuration file: vinor.config.json')
    click.echo('Initialized as vinor project successfully')


@click.command()
def init_db():
    click.echo('Initialized the database')


@click.command()
def drop_db():
    click.echo('Dropped the database')


# Configuration
@cli.command()
@click.option('--show', is_flag=True, flag_value=True, help='Show project configuration')
def config(show: bool):
    project_root = os.getcwd()
    initializer = Initializer(project_root)
    if show:
        if os.path.isfile(initializer.CONFIG_FILE):
            click.echo(json.dumps(initializer.read_config()))
        else:
            click.echo('Not found config file vinor.config.json')


cli.add_command(init)
cli.add_command(init_db)
cli.add_command(drop_db)


def main():
    cli()


"""
To see the commands run this:
    vinor --help 
"""
if __name__ == '__main__':
    main()
