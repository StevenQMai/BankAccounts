from bank_accounts import *

Hank = BankAccounts(initial_amount=1000, account_name="Hank")
Sara = BankAccounts(initial_amount=1000, account_name="Sara")

Hank.getBalance()
Sara.getBalance()

Sara.deposit(amount=500)
Hank.withdraw(amount=10000)
Hank.withdraw(amount=10)

Hank.transfer(amount=10000, account=Sara)
Hank.transfer(amount=10, account=Sara)

Jim = InterestRewardsAcc(initial_amount=1000, account_name="Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(amount=100, account=Hank)

Blaze = SavingsAcc(initial_amount=1000, account_name="Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sara)