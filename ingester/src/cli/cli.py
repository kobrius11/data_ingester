import click
from ingester.src.cli.new import new
from ingester.src.cli.sources import sources 

@click.group()
@click.help_option('-u', '--help')
def ingester():
    pass

ingester.add_command(new)
ingester.add_command(sources)