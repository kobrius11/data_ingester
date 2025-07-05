from abc import ABC, abstractmethod
from requests import Response

class AbstractClient(ABC):
    
    @abstractmethod
    def request(self, path: str, method: str) -> Response:
        pass