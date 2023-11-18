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

    def withdraw(self, value: float):
        if value > self.WITHDRAW_LIMIT or value < 0 or self.withdraw_limit_per_day == 0:
            return "Amount incorrect or limit per day"
        else:
            self.withdraw_limit_per_day -= 1
            self.balance -= value
            result = f"Draw out R${value}"
            self.__extract.add_extract(result)
            return result
