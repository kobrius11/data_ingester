from ingester.src.abstract import AbstractWriter
from kafka.producer import KafkaProducer
from typing import Any, Optional, Union, SupportsBytes, List, Tuple

class KafkaWriter(AbstractWriter, KafkaProducer):
    def __init__(self, **configs):
        super().__init__(**configs)
    
    def write(
            self,
            topic: str,
            value: Optional[Union[bytes, SupportsBytes]] = None,
            key: Optional[Union[bytes, SupportsBytes]] = None,
            headers: Optional[List[Tuple[str, bytes]]] = None,
            partition: Optional[int] = None,
            timestamp_ms: Optional[int] = None
        ):
        self.send(topic, value=value, key=key, headers=headers, partition=partition, timestamp_ms=timestamp_ms)

    def close(self, timeout=None, null_logger=False):
        super().close(timeout, null_logger)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.flush()
        self.close()
