# -*- coding: utf-8 -*-
from ingester.src.conf import Settings

from {{cookiecutter.classname_snake}}.cli import {{cookiecutter.classname_snake}}
from {{cookiecutter.classname_snake}}.client import client
from {{cookiecutter.classname_snake}}.endpoints import endpoints


SETTINGS_MODULE = '{{cookiecutter.classname_snake}}.settings'

settings = Settings(SETTINGS_MODULE)
cli_group = {{cookiecutter.classname_snake}}

__all__ = [
    "settings",
    "cli_group",
    "client",
    "endpoints"
]