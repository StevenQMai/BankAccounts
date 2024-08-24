class BalanceException(Exception):
    pass

class BankAccounts:
    def __init__(self, initial_amount, account_name) -> None:
        self.balance = initial_amount
        self.name = account_name
        print(f"Account '{self.name}' created.\n")

    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}.\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit complete!\n")
        self.getBalance() #since deposit and getBalance are both methods of the same class, they can access each other via 'self'

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}."
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount 
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}") 

    def transfer(self, amount, account):
        try:
            print(f"\n********\n\nBeginning Transfer...👺")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅ \n\n********")
        except BalanceException as error:
            print(f"\nTransfer Interrupted. ❌ {error}")

class InterestRewardsAcc(BankAccounts):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposit complete!")
        self.getBalance()

class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initial_amount, account_name) -> None:
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete!")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")