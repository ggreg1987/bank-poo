from datetime import date
from datetime import datetime
from Client import Client


class PhysicalPerson(Client):
    def __init__(self, name, date_birth, cpf,  account, address: dict):
        super().__init__(account, address)
        self.__name = name
        self.__date_birth = self.str_to_date(date_birth)
        self.__cpf = cpf

    def new_client(self, *args, **kwargs):
        self.__id += 1
        self.__accounts.append(args)
        for self.Client.__class__.__name__, self.__address in kwargs.items():
            return f"{self}: {self.__address}"
        return self.__id

    @classmethod
    def str_to_date(cls, data) -> date:
        return datetime.strptime(data, '%d/%m/%Y')
