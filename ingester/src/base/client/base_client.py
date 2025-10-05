from typing import Optional
from requests import Session
from ingester.src.abstract import AbstractClient
from ingester.src.base.endpoint import ClientEndpoints

class BaseClient(AbstractClient):
    endpoints = ClientEndpoints()

    def __init__(self, session: Optional[Session] = None, endpoints: list[str] = []):
        self.base_url = ""
        self.session = session if session is not None else Session()
        self.logger = None
        self.endpoints = endpoints
    
    # @property
    # def endpoints(self):
    #     return self._endpoint_descriptor.__get__(self, self.__class__)

    def request(self, path: str, method: str, **kwargs: dict[str, str]):
        """
        TODO: ERROR handling
        """
        res = self.session.request(method, path, **kwargs)

        return res