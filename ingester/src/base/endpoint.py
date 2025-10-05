import functools
from typing import TYPE_CHECKING, Callable, Any

if TYPE_CHECKING:
    from ingester.src.base import BaseClient
    from ingester.src.abstract import AbstractWriter


class Endpoint:
    def __init__(self, path: str, method: str):
        self.path = path
        self.method = method

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        self.func = func

        @functools.wraps(func)
        def __wrapper__(instance: "BaseClient", writer: "AbstractWriter", **kwargs: dict[str, str]) -> Callable[..., Any]:
            full_path = instance.base_url + self.path
            resp = instance.request(full_path, self.method, **kwargs)

            return func(instance, response=resp, writer=writer, **kwargs)
        return __wrapper__


class ClientEndpoints():

    def __get__(self, obj, objtype=None):
        # value = obj._endpoints
        # return value
        pass

    def __set__(self, obj, value):
        print(obj.endpoints)
        obj._endpoints = obj.endpoints
        # obj._endpoints.append(value)

