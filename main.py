from domain.models.Account import Account


class Main:
    __account = Account

    @classmethod
    def menu(cls):
        print(f"""
        CHOOSE YOUR OPTION

        1 - CREATE ACCOUNT
        2 - DEPOSIT
        3 - WITHDRAW
        4 - EXTRACT
        5 - EXIT
        """)

    def start(self):
        your_name = input("What's your name?")
        print(f"""
            Wellcome {your_name} to DIO's BANK!!!
            """)

        option = 0

        while option != 5:
            self.menu()
            option = int(input())
            match option:
                case 1:
                    name = input("Name")
                    date_birth = input("Birth day")
                    cpf = input("Cpf")
                    agency = input("Agency")
                    street = input("Street")
                    number = int(input("Number"))
                    new_account = self.__account.new_account(name, date_birth, cpf, agency, street, number)
                    print(new_account)

                case 2:
                    amount = float(input("How much you need?"))
                    result = self.__account.deposit(amount)
                    print(result)
