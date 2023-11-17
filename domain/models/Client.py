from abc import ABC


class Client(ABC):
    id: int = 0

    def __int__(self, account, address):
        self.__id = Client.id
        self.__accounts: list = account
        self.__address: dict = address

    @property
    def create_account(self, *args, **kwargs):
        self.__id += 1
        self.__accounts.append(args)
        for self.Client, self.__address in kwargs.items():
            return f"{self}: {self.__address}"

