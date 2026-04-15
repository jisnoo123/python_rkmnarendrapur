class Bank:

    def __init__(self, acc, holder, balance):
        self.acc = acc
        self.holder = holder
        self.__balance = balance    # Private variable
    
    def deposit(self, amount):
        if amount>=0:
            print(f'Depositing Rs.{amount}')
            self.__balance += amount
        else:
            print('Amount deposited cannot be negative')
    
    def withdraw(self, amount):
        if amount>=0:
            print(f'Withdrawing Rs.{amount}')
            self.__balance -= amount
        else:
            print('Amount withdrawn cannot be negative')
    
    def check_balance(self):
        print(f'Balance: Rs.{self.__balance}')

print('Enter details:')

account_holder = input('Account Holder: ')
account_num = int(input('Account Number: '))
balance = float(input('Account Balance: '))

obj = Bank(account_num, account_holder, balance)

amount_deposit = float(input('Enter amount to be deposited:'))
obj.deposit(amount_deposit)
obj.check_balance()

amount_withdrawn = float(input('Enter amount to be withdrawn: '))
obj.withdraw(amount_withdrawn)
obj.check_balance()