from datetime import date
from Client import Client


class PhysicalPerson(Client):
    def __init__(self, name, date_birth, cpf,  account, address):
        super().__init__(account, address)
        self.__name = name
        self.__date_birth = date_birth
        self.__cpf = cpf

    def new_client(self, *args, **kwargs):
        self.__id += 1
        self.__accounts.append(args)
        for self.Client, self.__address in kwargs.items():
            return f"{self}: {self.__address}"
        return self.__id
