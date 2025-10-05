from typing import Callable, Any, TYPE_CHECKING
from ingester.src.utils import register_endpoint_to_cli

if TYPE_CHECKING:
    import click


# register_endpoint_to_cli(client.latest, osrs_ge_wiki, "latest", WriterEnum.TEST_TOPIC())
class Path():
    """
    Path object is responsible for registering function to cli and
    providing a gateway to call function from code
    """

    def __init__(
            self,
            func: Callable[..., Any],
            cli_group: click.Group,
            func_name: str,
            writer: "Writer"
        ):
        self.func = func
        self.cli_group = cli_group
        self.func_name = func_name
        self.writer = writer
    
    def __call__(self):
        pass
    
    def register(self):
        register_endpoint_to_cli(self.func, self.cli_group, self.func_name, self.writer)