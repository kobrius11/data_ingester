from ingester.src.base import Endpoint
from ingester.src.utils import register_endpoint_to_cli
from {{ cookiecutter.classname_snake }} import client
from {{ cookiecutter.classname_snake }}.cli import {{ cookiecutter.classname_snake }}
from {{ cookiecutter.classname_snake }}.writers import WriterEnum

endpoints = [
    # register_endpoint_to_cli(client.example, {{ cookiecutter.classname_snake }}, "example_endp", WriterEnum.STDOUT()**kwargs)
]