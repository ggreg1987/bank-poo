from Extract import Extract
from PhysicalPerson import PhysicalPerson


class Account:
    balance: float
    WITHDRAW_LIMIT = 500
    withdraw_limit_per_day = 3

    def __int__(self, agency: str, client: PhysicalPerson):
        self.__agency = agency
        self.__client = client
        self.__extract = Extract()

    def new_account(self, name, date_birth, cpf, agency) -> int:
        return self.__client.new_client((name, date_birth, cpf, agency), {"street", "number"})
