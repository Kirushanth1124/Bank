correct_Account_Number = 74521031
correct_Customer_ID = "C001"
correct_username = "kirushanth"
correct_pasword = "dhanush123"




Account_number=input("Enter the Account number: ",correct_Account_Number)
Customer_ID=input("Enter the ID: ",correct_Customer_ID)
Username=input("Enter the name: ",correct_username)
Password=input("Enter the Password: ",correct_pasword)



file=open("Customer details.txt, 'w' ")
file.write(f"your Account number is: {Account_number}\n")
file.write(f"your your ID is: {Customer_ID}\n")
file.write(f"your Name is: {Username}\n")
file.write(f"your Password is: {Password}")
file.close()



















'''account_balances = [1000] 
selected_account = 0

while True:
    print("======ATM MENU======")
    print("01. Check Balance")
    print("02. Withraw money")
    print("03. Deposite Money")
    print("04. View all Account balance")
    print("05. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        print(f"Account {selected_account + 1} Balance: ${account_balances[selected_account]}")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= account_balances[selected_account]:
            account_balances[selected_account] -= amount
            print(f"Withdrawal successful. New balance: ${account_balances[selected_account]}")
        else:
            print("Insufficient funds!")

    elif choice == "3":
        deposit = float(input("Enter amount to deposit: $"))
        account_balances[selected_account] += deposit
        print(f"Deposit successful. New balance:${account_balances[selected_account]}")

    elif choice == "4":
        print("\n📋 All Account Balances:")
        for i, balance in enumerate(account_balances):
            print(f"Account {i + 1}: ${balance}")
        print()

    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.\n")'''







#         max_attempt = 3
# attempt = 0

# while attempt < max_attempt:
#     username = input("Enter your user name: ")
#     password = input("enter your password: ")
#     if username == correct_username and password == correct_pasword:
#         print("Login Successfull")
#         break
#     else:
#         attempt += 1
#         remaining = max_attempt - attempt
    
#         print("Failed login")

# if attempt == max_attempt:
#     print(" not valid failed")
#     exit()