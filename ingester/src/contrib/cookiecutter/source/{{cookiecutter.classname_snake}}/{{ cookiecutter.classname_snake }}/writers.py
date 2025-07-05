import sys
from enum import Enum
from ingester.src.base.writer import FileWriter

class WriterEnum(Enum):
    STDOUT = lambda: FileWriter(sys.stdout)
    OUTPUT_JSON = lambda: FileWriter(open("output.json", "w"))

    def __call__(self):
        return self.value()