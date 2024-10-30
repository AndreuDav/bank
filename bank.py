class BankAccount:

    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
        self.transaction_history = []


    def deposit(self, amount):
        self.balance = amount
        print('Вы пополнили баланс!')
        self.transaction_history.append(f'+ {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств!')
        else:
            self.balance -= amount
            self.transaction_history.append(f"-{amount}")
            print('Сумма снята!')

    def display_balance(self):
        print('баланс вашей карты:', self.balance)

    def get_transaction_history(self):
        print(self.transaction_history)


andrey_bank = BankAccount(account_number = 1111, balance = 0, account_holder = 'Andrey Denisov')
andrey_bank.display_balance()
andrey_bank.deposit(100)
andrey_bank.withdraw(100)
andrey_bank.display_balance()
andrey_bank.get_transaction_history()