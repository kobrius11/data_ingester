from typing import Any
from pathlib import Path
import click
from cookiecutter.main import cookiecutter
from ingester.src.conf import settings
from ingester.src.utils import to_snake_case

@click.group()
def new():
    """
    Create object templates
    """
    pass

@new.command()
@click.option(
    '-o',
    '--output',
    help="Location where data-source will be generated",
    default='./sources/',
)
def source(output: str):
    """
    Create new data-source
    """
    template_loc: Path = settings.ROOT_PATH / Path("src/contrib/cookiecutter/source/")

    click.echo("\n")
    name = click.prompt("data-source name")
    author = click.prompt("data-source author's name")
    email = click.prompt("data-source author's email")
    version = click.prompt("data-source version")
    classname = click.prompt("Entrypoint classname")
    base_url = click.prompt("data-source base url")

    context: dict[str, Any] = {
        "project": name,
        "author": author,
        "author_email": email,
        "version": version,
        "classname": classname,
        "classname_snake": to_snake_case(classname),
        "base_url": base_url,
        "_source": "cli",
    }
    
    output_dir = Path(output)
    if not output_dir.is_absolute():
        cwd = Path.cwd()
        output_dir = Path(cwd / output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)

    cookiecutter(
        str(template_loc.resolve()),
        no_input=True,
        extra_context=context,
        output_dir=str(output_dir.resolve())
    )

    click.echo(u"\nWritten: {}".format(str(output_dir.resolve())))