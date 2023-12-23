from typing import Tuple, Optional

import config
from src.clients.client import Client
from src.rcp_client import RcpClient


def client_handler():
    host = config.HOST
    port = config.PORT

    client = Client(host, port)
    RcpClient(client=client).run()


if __name__ == "__main__":
    client_handler()
