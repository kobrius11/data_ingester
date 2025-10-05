import logging
from ingester.src.base import BaseClient
from ingester.src.base.endpoint import ClientEndpoints


client = BaseClient()
# client.endpoints.append("hello")




if __name__ == "__main__":
    # ingester()
    print(client.endpoints)
