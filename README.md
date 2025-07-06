# Data ingester

This library aims to standartize data collection process from variuos endpoints, by defining standart way of receiving, writing, storing data. its meant to be used along with cronjobs inside linux container.

## Setting up
Right data-ingester project is at very early stage, so pypi repository is not yet live, so to install data-ingester you must clone it and install by hand.
Install with editable mode if you plan to make changes to the core ingester codebase.

```sh
# first clone the ingester into your project
git clone {ingester}

# ../your_project/ingester/
pip install .
# or
pip install -e . # for editable mode
```

## Usage
Once ingester is set up you can use it with command-line (or cli for short)

```sh
# should print out available commands and their comments
ingester

# used for creating a new data-source
ingester new source 

# once data source is created yuou can acess its endpoints using
ingester sources {data-source-classname_snake_case} 
```

## defining an endpoint
Once you created a new data-source, you will find its core code at default location {./sources/data-source-classname_snake_case} notice that this directory has a pyproject.toml file inside, which means you must add this project to your PYTHONPATH. Recomended way to do that is just install it as editable package like so:

```sh
# move to your data-source dir
cd ./sources/{data_source}

# install it as editable package (adding it to PYTHONPATH)
pip install -e .
```

Once that is done you can define an endpoint in ./sources/{data-source}/{data-source}/client.py 

for example: 
A simple endpoint that writes into standart output

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ./sources/{data-source}/{data-source}/client.py
from typing import Optional, TYPE_CHECKING
from requests import Session
from ingester.src.base import BaseClient
from ingester.src.base import Endpoint
import json

if TYPE_CHECKING:
    from requests import Response
    from ingester.src.abstract import AbstractWriter


class OsrsGeWiki(BaseClient):
    
    def __init__(self, session: Optional[Session] = None) -> None:
        super().__init__(session)
        self.base_url: str = "https://prices.runescape.wiki/api/v1/osrs/"
    
    @Endpoint("latest", "GET")
    def latest(self, response: "Response", writer: "AbstractWriter", **kwargs):
        with writer:
            writer.write(respose.text + "\n")

client = OsrsGeWiki()
```

then you must define a writer which is created at ./sources/{data-source}/{data-source}/writers.py
as you can see there a few common ones already predefined

```python
# ./sources/{data-source}/{data-source}/writers.py
import sys
from enum import Enum
from ingester.src.base.writer import FileWriter, KafkaWriter

class WriterEnum(Enum):
    STDOUT = lambda: FileWriter(sys.stdout)
    OUTPUT_JSON = lambda: FileWriter(open("output.json", "w"))

    def __call__(self):
        return self.value()
```

And the last thing you must register this endpoint to command-line interface or CLI
like so: 

```python
# ./sources/{data-source}/{data-source}/endpoints.py
from ingester.src.base import Endpoint
from ingester.src.utils import register_endpoint_to_cli
from osrs_ge_wiki import client
from osrs_ge_wiki.cli import osrs_ge_wiki
from osrs_ge_wiki.writers import WriterEnum

endpoints = [
    register_endpoint_to_cli(client.latest, osrs_ge_wiki, "latest", WriterEnum.STDOUT())
]
```

and now this endpoint becomes available at:
```sh
ingester sources {data_source} latest
```

and once this command is executed it should pass response output to its writer AKA standart output in our case.

