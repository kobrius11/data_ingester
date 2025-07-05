import io
import sys
from typing import Any
from ingester.src.abstract import AbstractWriter

class FileWriter(AbstractWriter):
    def __init__(self, file: io.TextIOWrapper):
        self.file = file

    def write(self, data: Any):
        self.file.write(data)
    
    def close(self):
        if not self.file.closed and self.file not in (sys.stdout, sys.stderr, sys.stdin):
            self.file.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()