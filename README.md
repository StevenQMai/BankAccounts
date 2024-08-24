# Bank Accounts 
A simple banking application that simulates numerous users utilizing various banking features

## Table of Contents
1. [Account Types](#account-types)
2. [Application Features](#application-features)


## Account Types

The application supports different types of bank accounts:

- **Standard Bank Account:** 
  - Basic account type where you can deposit, withdraw, and transfer funds.
  
- **Interest Rewards Account:** 
  - Inherits from the standard account, offering a 5% bonus on deposits.
  
- **Savings Account:** 
  - Inherits from the interest rewards account, but includes a $5 withdrawal fee.


## Application Features

• **Account Creation:**
  - Easily create different types of accounts such as:
    - `BankAccounts`: Standard bank account.
    - `InterestRewardsAcc`: Bank account with interest rewards.
    - `SavingsAcc`: Savings account with withdrawal fees.

• **Error Handling:**
  - **BalanceException:** Custom exception raised when attempting to withdraw or transfer more money than the available balance.

• **Deposit and Withdrawal:**
  - **Deposit:** Add money to any account using the `deposit` method.
  - **Withdraw:** Safely withdraw funds using the `withdraw` method, with built-in checks to prevent overdrafts.

• **Transfers Between Accounts:**
  - **Transfer:** Move funds between different accounts, ensuring sufficient balance before completing the transaction.


