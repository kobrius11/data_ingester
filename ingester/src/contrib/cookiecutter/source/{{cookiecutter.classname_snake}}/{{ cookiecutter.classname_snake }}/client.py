#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional, TYPE_CHECKING
from requests import Session
from ingester.src.base import BaseClient
from ingester.src.base import Endpoint

if TYPE_CHECKING:
    from requests import Response
    from ingester.src.abstract import AbstractWriter


class {{ cookiecutter.classname }}(BaseClient):
    
    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__(session)
        self.base_url: str = "{{ cookiecutter.base_url }}"
    
    # @Endpoint("example_point", "GET")
    # def example_point(self, response: "Response", writer: "AbstractWriter", **kwargs):
    #    with writer:
    #         writer.write(response.text + '\n')

client = {{ cookiecutter.classname }}()