from abc import ABC
from datetime import datetime


class Client:
    id: int = 1

    def __int__(self, *args, **kwargs):
        self.__id = Client.id
        self.__accounts: list = args
        self.__address: dict = kwargs
