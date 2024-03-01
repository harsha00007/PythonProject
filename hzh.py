# from tkinter import *
#
# master = Tk()
#
#
# def callback():
#     print("you clicked the button")
#
#
# btn = Button(master, text="ok", command=callback)
# btn.pack()
# mainloop()


import random

class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.account_number = random.randint(10000, 200000)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Deposit successful")

    def get_balance(self):
        return self.balance

def create_account():
    name = input("Enter your name: ")
    initial_deposit = int(input("Enter initial deposit: "))
    if initial_deposit <= 0:
        print("Invalid initial deposit amount")
        return None
    return BankAccount(name, initial_deposit)

def access_account(accounts):
    name = input("Enter your name: ")
    acc_no = int(input("Enter your account number: "))
    account = next((acc for acc in accounts if acc.name == name and acc.account_number == acc_no), None)
    if account:
        while True:
            print("Enter 1 to withdraw")
            print("Enter 2 to deposit")
            print("Enter 3 to display balance")
            print("Enter 4 to exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 3:
                print(f"Available balance: {account.get_balance()}")
            elif choice == 4:
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid name or account number")

def main():
    accounts = []
    while True:
        print("Enter 1 to create a new account")
        print("Enter 2 to access an existing account")
        print("Enter 3 to exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            account = create_account()
            if account:
                accounts.append(account)
        elif choice == 2:
            access_account(accounts)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
