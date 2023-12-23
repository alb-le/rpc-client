import config
from src.clients.client import Client


class RcpClient:
    def __init__(self, client: Client):
        self.client = client

    def run(self):
        print(f'Started RCP as Client. Address: {self.client}')
        print(f'Write a request. You might try "help()" or "exit():"')
        running = True
        self.client.handshake()

        while running:
            try:
                self.__run()

            except KeyboardInterrupt:
                self.client.close()
                print(f'[INFO] Server {self.client} interrupted.')
                break

            except Exception as ex:
                print(f'[ERROR] Closing client because of an error:')
                self.client.close()
                raise ex

    def __run(self):
        user_input = self.__get_input()
        fn_name, args, kwargs = user_input

        res = self.client.call_fn(fn_name, args, kwargs)
        print(res)

    @staticmethod
    def __get_input():
        s = input()
        fn_name = s.split('(')[0]
        args = s[len(fn_name)+1:-1].strip(' ').split(',')
        kwargs = {}
        if fn_name == 'exit':
            raise KeyboardInterrupt
        return fn_name, args, kwargs
