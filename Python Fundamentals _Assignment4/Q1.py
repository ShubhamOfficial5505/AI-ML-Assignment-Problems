class BankAccount:
    def __init__(self, owner_name, account_number, balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit_balance(self, amount):
        self.balance += amount

    def withdraw_balance(self, amount):
        if(amount > self.balance):
            print("Not enough balance")
        else:
            self.balance -= amount

    def check_balance(self):
        print(f"Your account balance is { self.balance }")

bank_acc = BankAccount("Shubham Kar", "98765432", 45000)
bank_acc.deposit_balance(15000)
bank_acc.check_balance()
bank_acc.withdraw_balance(65000)
bank_acc.withdraw_balance(35000)
bank_acc.check_balance()