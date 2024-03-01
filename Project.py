import random


class Create_new_account:
    def __init__(self):
        self.name = None
        self.balance = None
        self.account_number = None

    def account_create(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(10000, 200000)
        print(f"Account creation has been successful your account number is ==> {self.account_number}")

    def withdraw(self, amount_withdraw):
        self.balance -= amount_withdraw
        print("Amount Withdraw is successful from your Account\n")

    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print(f"Amount Deposit is successful to your Account\n")

    def balance_amount(self):
        return self.balance


new_account = Create_new_account()
while True:
    print("Enter 1 to create new account")
    print("Enter 2 access an exiting account")
    print("Enter 3 to exit")
    user_input = int(input("Enter: \n"))
    if user_input == 1:
        user_name = input("Enter your name: \n")
        initial_deposit = int(input("Enter initial deposit: \n"))
        if initial_deposit > 0:
            new_account.account_create(user_name, initial_deposit)
        else:
            print("Enter a valid Amount")

    elif user_input == 2:
        name = input("Enter your name: \n")
        acc_no = int(input("Enter your account number: \n"))
        while True:
            if name == new_account.name and acc_no == new_account.account_number:
                print("Enter 1 to Withdraw")
                print("Enter 2 to Deposit")
                print("Enter 3 to display the available balance")
                print("Enter 4 to previous menu")
                inpt = int(input("Enter a number: \n"))
                if inpt == 1:
                    enter_amount = int(input("Enter the amount to withdraw: \n"))
                    if enter_amount > new_account.balance_amount():
                        print(f"Insufficient balance\nBalance is Only {new_account.balance_amount()}\n")
                    else:
                        new_account.withdraw(enter_amount)
                        new_account.balance_amount()
                elif inpt == 2:
                    enter_amount = int(input("Enter the amount to deposit: \n"))
                    new_account.deposit(enter_amount)
                    new_account.balance_amount()
                elif inpt == 3:
                    print(f"Available balance is {new_account.balance_amount()}\n")

                elif inpt == 4:
                    break
                else:
                    print("Enter a correct number")
            else:
                print("Invalid name or account number")
                break
    elif user_input == 3:
        break
    else:
        print("Enter a correct number")

