import random
from datetime import datetime

Accounts = {}

def load_accounts():
    
    try:
        with open("Create Account detail.txt", "r") as file:
            for line in file:
                parts = line.strip().split("---")
                if len(parts) == 5:
                    account_number, name, user_name, user_password, balance = parts
                    Accounts[account_number] = {
                        "Name": name,
                        "UserName": user_name,
                        "Password": user_password,
                        "Balance": float(balance),
                        "Transactions": []
                    }
    except FileNotFoundError:
        pass

def save_account_to_file(account_number, name, user_name, user_password, initial_balance):
    
    with open("Create Account detail.txt", 'a') as file:
        file.write(f"{account_number}---{name}---{user_name}---{user_password}---{initial_balance:.2f}\n")

def append_login_credentials(username, password, role="user"):
    
    with open("login.txt", "a") as file:
        file.write(f"{username}---{password}---{role}\n")

def login():
    
    print("\n::::::===== Login =====::::::\n")
    username = input("* Enter your username  🫴  : ")
    password = input("* Enter your password  🫴  : ")

    try:
        with open("login.txt", "r") as file:
            for line in file:
                parts = line.strip().split("---")
                if len(parts) == 3:
                    saved_user, saved_pass, role = parts
                    if username == saved_user and password == saved_pass:
                        print(f"\n☑️ Login successful! Welcome {username}\n")
                        return role, username  
            print("\nPlease enter Correct username or password  👎 .\n")
            return None, None
    except FileNotFoundError:
        print("❌ login.txt file not found")
        return None, None

def Adminmenu():
    
    while True:
        print("\n|===== Admin Banking Menu ======|\n")
        print("1. Create Account.........")
        print("2. Deposit Money..........")
        print("3. Withdraw Money.........")
        print("4. Check Balance..........")
        print("5. Transaction History....")
        print("6. Transfer Money.........")
        print("7. Change password........")
        print("8. Exit...................")

        choice = input("\n🆗 Choose your option (1-8): ")
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
            Change_Password()
        elif choice == "8":
            print("\n☑️ Thank you for using our admin services  🙏 .\n")
            break
        else:
            print("\n❌ Invalid choice.\n")

def usermenu():
    
    while True:
        print("\n|===== User Banking Menu ======|\n")
        print("1. Deposit Money..........")
        print("2. Withdraw Money.........")
        print("3. Check Balance..........")
        print("4. Transaction History....")
        print("5. Transfer Money.........")
        print("6. Change Password........")
        print("7. Exit...................")

        choice = input("\n🆗  Choose your option (1-7): ")
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
            Change_Password()
        elif choice == "7":
            print("\n✅ Thank you for using our service  🙏 .\n")
            break
        else:
            print("\n❌ Invalid choice.\n")

def Create_Account():
    
    name = input("* Enter Account Holder Name  🫴 : ")
    user_name = input("* Enter Username  🫴 : ")
    user_password = input("* Enter Password  🔑 : ")

    while True:
        try:
            initial_balance = float(input("* Enter Initial Balance: "))
            if initial_balance < 0:
                print("\nInitial balance must be non-negative.\n")
                continue
            break
        except ValueError:
            print("\nInvalid input. Enter a numeric value.\n")

    account_number = str(random.randint(100000, 999999))
    while account_number in Accounts:
        account_number = str(random.randint(100000, 999999))

    Accounts[account_number] = {
        "Name": name,
        "UserName": user_name,
        "Password": user_password,
        "Balance": initial_balance,
        "Transactions": []
    }

    save_account_to_file(account_number, name, user_name, user_password, initial_balance)
    append_login_credentials(user_name, user_password)  

def Deposit_Money():
    
    account_number = input("* Enter your Account Number  🔢 : ")

    if account_number not in Accounts:
        print("\n❌ Account not found.\n")
        return
    try:
        amount = float(input("* Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        Accounts[account_number]["Balance"] += amount
        Accounts[account_number]["Transactions"].append(f"Deposited ${amount:.2f}")
        
        print(f"✅ \nDeposited successfully. New Balance: ${Accounts[account_number]['Balance']:.2f}\n")
    except ValueError:
        print("\n❌ Invalid amount.\n")

def Withdraw_Money():
    
    account_number = input("* Enter your Account Number  🔢 : ")
    if account_number not in Accounts:
        print("\nAccount not found.\n")
        return
    try:
        amount = float(input("* Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > Accounts[account_number]["Balance"]:
            print("🚫 Insufficient balance.")
            return
        Accounts[account_number]["Balance"] -= amount
        Accounts[account_number]["Transactions"].append(f"Withdraw ${amount:.2f}")
        print(f"\n🆗 Withdrawal successful. New Balance: ${Accounts[account_number]['Balance']:.2f}\n")
        
    except ValueError:
        print("\n❌ Invalid amount.\n")

def Check_Balance():
    
    account_number = input("* Enter your Account Number  🔢 : ")
    if account_number not in Accounts:
        print("\n❌ Account not found.\n")
        return
    print(f"\n* Current Balance: ${Accounts[account_number]['Balance']:.2f}\n")

def Transaction_History():
    
    account_number = input("* Enter your Account Number  🔢 : ")
    if account_number not in Accounts:
        print("\n❌ Account not found.\n")
        return
    Transactions = Accounts[account_number]["Transactions"]
    if not Transactions:
        print("❌No transactions found.")
        return
    print("* Transaction History:")
    for t in Transactions:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{now}-- {t}")

def Transfer_Money():
    
    from_acc = input("* Enter your Account Number  🔢 : ")
    if from_acc not in Accounts:
        print("\nSender account not found.\n")
        return
    to_acc = input("* Enter recipient Account Number: ")
    if to_acc not in Accounts:
        print("\n🚫 Recipient account not found.\n")
        return
    try:
        amount = float(input("* Enter amount to transfer: "))
        if amount <= 0:
            print("\nAmount must be positive.\n")
            return
        if amount > Accounts[from_acc]["Balance"]:
            print("\nInsufficient balance.\n")
            return
        Accounts[from_acc]["Balance"] -= amount
        Accounts[to_acc]["Balance"] += amount
        Accounts[from_acc]["Transactions"].append(f"Transferred ${amount:.2f} to {to_acc}")
        Accounts[to_acc]["Transactions"].append(f"Received ${amount:.2f} from {from_acc}")
        print(f"Transfer successful. ${amount:.2f} transferred from {from_acc} to {to_acc}")
    except ValueError:
        print("\n🚫 Invalid amount  👎 .\n")

def Change_Password():
    
    USERNAME = input("* Enter the Username  🫴 : ")  
    Old_Password = input("* Enter the Current Password   🔑 : ")

    updated_lines = []
    found = False  
    try:
        with open("login.txt", 'r') as file:
            for line in file:
                parts = line.strip().split("---")
                if len(parts) != 3:
                    updated_lines.append(line)
                    continue
                
                saved_user, saved_pass, role = parts
                if USERNAME == saved_user and Old_Password == saved_pass:
                    New_password = input("\n* Enter the New password  🔑 : \n") 
                    updated_lines.append(f"{USERNAME}---{New_password}---{role}\n")
                    found = True
                else:
                    updated_lines.append(line)

        if found:
            with open("login.txt", 'w') as file:
                file.writelines(updated_lines)
                print("\n🆗 Password Changed Successfully  👍 \n")
        else:
            print("\nIncorrect username or password  😠 .\n") 

    except FileNotFoundError:
        print("🚫 Error: login.txt file not found  👎 ")

def main():
    
    load_accounts()
    role, username = login()
    if role is None:
        print("\nLogin failed. Exiting  🙋‍♂️ .\n")
        return
    
    if role == "admin":
        Adminmenu()
    else:
        usermenu()

main()


