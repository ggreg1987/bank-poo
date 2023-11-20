from Extract import Extract
from PhysicalPerson import PhysicalPerson


class Account:
    balance: float
    WITHDRAW_LIMIT = 500
    withdraw_limit_per_day = 3

    def __int__(self, agency: str, client: PhysicalPerson, extract: Extract):
        self.__agency = agency
        self.__client = client
        self.__extract = extract

    def new_account(self, name, date_birth, cpf, agency, street, number):
        account: tuple = (name, date_birth, cpf, agency)
        address: dict = {"street": street, "number": number}
        return self.__client.new_client(account, address)

    def withdraw(self, value: float):
        if value > self.WITHDRAW_LIMIT or value < 0 or self.withdraw_limit_per_day == 0:
            return "Amount incorrect or limit per day"
        else:
            self.withdraw_limit_per_day -= 1
            self.balance -= value
            result = f"Draw out R${value}"
            self.__extract.add_extract(result)
            return result

    def deposit(self, value: float):
        if value > 0:
            self.balance += value
            result = f"deposited R${value}"
            self.__extract.add_extract(result)
            return result
        else:
            return "Amount incorrect"

    def extract(self):
        self.__extract.extract_list()
