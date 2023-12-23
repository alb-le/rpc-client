import json

import config
from src.clients.socket_client import SocketClient


class Client(SocketClient):
    def __init__(self, host: str = None, port: int = None):
        super().__init__(host, port)
        self.server_address = (host, config.SERVER_PORT)

    def handshake(self):
        self.socket.connect(self.server_address)

    def call_fn(self, fn_name, args, kwargs):
        self.socket.sendall(json.dumps((fn_name, args, kwargs)).encode())
        res = self.socket.recv(config.MSG_SIZE).decode()
        return json.loads(res)
