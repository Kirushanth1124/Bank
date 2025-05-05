import random
from datetime import datetime

Accounts = {}

def load_accounts():
    try:
        with open("Create Account detail.txt", "r") as file:
            for line in file:
                account_number, name, balance = line.strip().split(":")
                Accounts[account_number] = {
                    "Name": name,
                    "Balance": float(balance),
                    "Transactions": []}
    except FileNotFoundError:
        pass

def save_account_to_file(account_number, name, balance):
    with open("Create Account detail.txt", 'a') as file:
        file.write(f"{account_number}:{name}:{balance:.2f}\n")

def login():
    
    print("\n===== Welcome to the Banking System Login =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open("login.txt", "r") as file:
         for line in file:
            parts = line.strip().split(':')
            if len(parts) == 3:
                saved_user, saved_pass, role = parts
                username==saved_user and password==saved_pass
            else:
                print(f"Skipping invalid line: {line}")
                if role == "admin":
                    Adminmenu()
                elif role == "user":
                    usermenu()
                else:
                    print("Unknown role. Access denied.")
                return  
            print("Invalid username or password. Please try again.")
    except FileNotFoundError:
        print("Error: login.txt file not found.")
        
def Adminmenu():
    while True:
        print("\n===== Admin Banking Menu ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("Choose your option (1-7): ")
        if choice == "1":
            Create_Account()
        elif choice == "2":
            Deposit_Money()
        elif choice == "3":
            Withdraw_Money()
        elif choice == "4":
            Check_Balance()
        elif choice == "5":
            Transaction_History()
        elif choice == "6":
            Transfer_Money()
        elif choice == "7":
            print("Thank you for using our admin services.")
            break
        else:
            print("Invalid choice.")

def usermenu():
    
    while True:
        print("\n===== User Banking Menu ======")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Choose your option (1-6): ")
        if choice == "1":
            Deposit_Money()
        elif choice == "2":
            Withdraw_Money()
        elif choice == "3":
            Check_Balance()
        elif choice == "4":
            Transaction_History()
        elif choice == "5":
            Transfer_Money()
        elif choice == "6":
            print("Thank you for using our service.")
            break
        else:
            print("Invalid choice.")

def Create_Account():
    name = input("Enter Account Holder Name: ")
    user_name = input("Enter Username: ")
    user_password = input("Enter Password: ")

    while True:
        try:
            initial_balance = float(input("Enter Initial Balance: "))
            if initial_balance < 0:
                print("Initial balance must be non-negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    account_number = str(random.randint(100000, 999999))
    while account_number in Accounts:
        account_number = str(random.randint(100000, 999999))

    Accounts[account_number] = {
        "Name": name,
        "Balance": initial_balance,
        "Transactions": []}

    save_account_to_file(account_number, name, user_name, user_password, initial_balance)
    append_login_credentials(user_name, user_password)  

def save_account_to_file(account_number, name, user_name, user_password, initial_balance):
    with open("Create Account detail.txt", 'a') as file:
        file.write(f"{account_number}:{name}:{user_name}:{user_password}:{initial_balance:.2f}\n")

    print(f"Account created successfully. Account Number: {account_number}")


def append_login_credentials(username, password, role="user"):
    with open("login.txt", "a") as file:
        file.write(f"{username}:{password}:{role}\n")

def Deposit_Money():
    
    account_number = input("Enter your Account Number: ")
    if account_number not in Accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        Accounts[account_number]["Balance"] += amount
        Accounts[account_number]["Transactions"].append(f"Deposited ${amount:.2f}")
        print(f"Deposited successfully. New Balance: ${Accounts[account_number]['Balance']:.2f}")
    except ValueError:
        print("Invalid amount.")

def Withdraw_Money():
    
    account_number = input("Enter your Account Number: ")
    if  account_number not in Accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > Accounts[account_number]["Balance"]:
            print("Insufficient balance.")
            return
        Accounts[account_number]["Balance"] -= amount
        Accounts[account_number]["Transactions"].append(f"Withdrew ${amount:.2f}")
        print(f"Withdrawal successful. New Balance: ${Accounts[account_number]['Balance']:.2f}")
    except ValueError:
        print("Invalid amount.")

def Check_Balance():
    
    account_number = input("Enter your Account Number: ")
    if account_number not in Accounts:
        print("Account not found.")
        return
    print(f"Current Balance: ${Accounts[account_number]['Balance']:.2f}")


def Transaction_History():
    
    account_number = input("Enter your Account Number: ")
    if account_number not in Accounts:
        print("Account not found.")
        return
    transactions = Accounts[account_number]["Transactions"]
    if not transactions:
        print("No transactions found.")
        return
    print("Transaction History:")
    for t in transactions:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{now}- {t}")

def Transfer_Money():
    
    from_acc = input("Enter your Account Number: ")
    if from_acc not in Accounts:
        print("Sender account not found.")
        return
    to_acc = input("Enter recipient Account Number: ")
    if to_acc not in Accounts:
        print("Recipient account not found.")
        return
    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > Accounts[from_acc]["Balance"]:
            print("Insufficient balance.")
            return
        Accounts[from_acc]["Balance"] -= amount
        Accounts[to_acc]["Balance"] += amount
        Accounts[from_acc]["Transactions"].append(f"Transferred ${amount:.2f} to {to_acc}")
        Accounts[to_acc]["Transactions"].append(f"Received ${amount:.2f} from {from_acc}")
        print(f"Transfer successful. ${amount:.2f} transferred from {from_acc} to {to_acc}")
    except ValueError:
        print("Invalid amount.")


load_accounts()
# login()
# Create_Account()