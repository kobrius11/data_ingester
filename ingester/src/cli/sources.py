import click
from ingester.src.utils import find_sources

@click.group()
def sources():
    pass

for source, module in find_sources().items():
    sources.add_command(module.cli_group)