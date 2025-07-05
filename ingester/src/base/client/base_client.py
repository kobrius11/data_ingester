from typing import Optional
from requests import Session
from ingester.src.abstract import AbstractClient

class BaseClient(AbstractClient):
    def __init__(self, session: Optional[Session] = None):
        self.base_url = ""
        self.session = session if session is not None else Session()
        self.logger = None
    
    def request(self, path: str, method: str, **kwargs: dict[str, str]):
        """
        TODO: ERROR handling
        """
        res = self.session.request(method, path, kwargs)

        return res