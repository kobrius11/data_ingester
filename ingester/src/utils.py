import re
from typing import Callable, Any, TYPE_CHECKING
import click

if TYPE_CHECKING:
    from ingester.src.abstract import AbstractWriter



def find_sources():
    import importlib.metadata

    entries = importlib.metadata.entry_points(group="ingester.plugins")
    plugins = {ep.name: ep.load() for ep in entries}
    return plugins

def to_snake_case(text: str) -> str:
    text = re.sub(r'[\W]+', '_', text)
    text = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', text)

    return text.lower().strip('_')

def register_endpoint_to_cli(
    func: Callable[..., Any],
    cli_group: click.Group,
    name: str,
    writer: "AbstractWriter",
    **kwargs
) -> None:
    
    @click.command(name=name)
    @click.pass_context
    def command(ctx, **cli_args):
        return func(writer=writer, **cli_args, **kwargs)

    cli_group.add_command(command)