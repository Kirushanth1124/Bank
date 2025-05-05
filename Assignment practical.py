import random

Accounts={}

def Menu():
    while True:
        print("\n=====Banking System======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Transfer Money(Bonus)")
        print("7. Exit")

Choice=input("Choose your option(1-7): ")

if Choice=="1":
 def Create_Account():
    Account_Number=str(87748569)
    Account_Holder_Name=input("Enter Account Holder's Name: ")

    while True:
        try:
            Initial_balance=float(input("Enter Initial Balance: "))
            if Initial_balance<0:
                ValueError("Intial Balance must be non Nagative")
                break
        except ValueError as e:
            print(e)

    Accounts[Account_Number]={"Account_Holder":Account_Holder_Name,"Balance":Initial_balance,"transaction":[]}
    print("Account create Successsfuly..Acccount Number: {Account_Number}")





if Choice=="2":
 def Deposit_Money():
    Account_Number=input("Enter your Account Number: ")
    if Account_Number not in Accounts:
        print("Account NOt Found")
        return
    while True:
        try:
            Deposit_Amount=float(input("Enter the Deposit Amount: "))
            if Deposit_Amount<=0:
                ValueError("Deposit Amount must be positive ")
                break
        except ValueError as e :
            print(e)

    Accounts[Account_Number]["Balance"]+=Deposit_Amount
    Accounts[Account_Number]["transactions"].append(f"Deposited: ${Deposit_Amount}")

if Choice=="3": 
 def Withdraw_Money():
    Account_Number=input("Enter your Account Number: ")
    if Account_Number not in Accounts:
        print("Account not Found")
        return
    while True:
        try:
            Withdraw_Amount=float(input("Enter the Withdraw Amoubt: "))
            if Withdraw_Amount<=0:
                ValueError("Withdraw Amount must be positive")
                if Withdraw_Amount>Accounts[Account_Number]["Balance"]:
                    ValueError("Insuffucent Balance")
                    break
        except ValueError as e:
            print(e)

    Accounts[Account_Number]["Transactions"].append(f" Withdraw Amount:$ {Withdraw_Amount}")
    print(f"${Withdraw_Amount} Withdraw Successfuly. And New Balance is: ${Accounts[Account_Number]["Balance"]}")

if Choice=="4":
 def Check_Balance():
    Account_Number=input("EWnter your Account Number: ")
    if Account_Number not in Accounts:
        print("this Account not Found")
        return
    print(f"Account Balance: $ {Accounts[Account_Number]["Balance"]}")

if Choice=="5":
 def Transection_History():
    Account_Number=input("Enter your Account Number: ")
    if Account_Number not in Accounts:
        print("This Account is Not Found")
        return 
    if not Accounts[Account_Number]["Transactions"]:
        print("no transaction found")
        return
    print("Transaction History: ")
    for Transaction in Accounts[Account_Number]["Transaction"]:
        print(Transaction)

if Choice=="6":
 def Transfer_Money():
    From_Account=input("Enter your Account Number: ")
    if From_Account not in Accounts:
       print("Your Account is NOt Found")
       return
    To_Account=input("Enter reciever Account Number: ")
    if To_Account not in Accounts:
       print("This Account not found .Invalid Account")


    while True:
        try:
          Transfer_Amount=float(input("Enter the Transfer Amount: "))
          if Transfer_Amount<=0:
             ValueError("Transfer Amoiunt mus be Positive")
             if Transfer_Amount> Accounts[From_Account]["Balance"]:
                ValueError("Insufficent ")
                break
        except ValueError as e:
           print(e)

    Accounts[From_Account]["Balance"]-=Transfer_Amount

    Accounts[To_Account]["Balance"]+=Transfer_Amount

    Accounts[From_Account]["Transactions"].append(f" Transfered: ${Transfer_Amount}to{To_Account}")

    Accounts[To_Account]["Transactions"].append(f"recieved: $ {Transfer_Amount}from{From_Account}")

    print(f"$ {Transfer_Amount} And Tranfer Successfuly")

if Choice=="7":
   print("Thank you for use ousr Service")   
   exit()

if __name__=="__main":
   Menu()





    




































# Account=[0]

# def Creat_Account():

#     if Student_Correct_Username in Account:
#         print("Username Registered")
#         return 
#     if Student_Correct_Age <18:
#         print("You Are Child ")
#     else:
#         print("Please invalid Age this is a Student Account" )

# Student_Correct_Name=input("Select the Name: ")   
# Student_Correct_Age=(input("Select the Age: "))
# Student_Correct_DOB=(input("Select the DOB: ")) 
# Student_Correct_Username =input("Select your Username: ")
# Student_Correct_Password=input("Select the Password: ")
# print("Account Created!!")


# Amount=(input("And Please Deposit your Beginnig payment: "))
# Account+=Amount
# print(f"Ok thank you!! Deposit Successful And your New Balance is : {Account}")

# def Login():

#     print(f"Party Name is : {Student_Correct_Name}" )
#     print(f"Party Age is : {Student_Correct_Age}" )
#     print(f"Party DOB is : {Student_Correct_DOB}" )
#     Username=input("Re-enter your Username: ")
#     Password=input("Re-enter your Password: ")
    
#     if Password==Student_Correct_Password and Username==Student_Correct_Username :
#         print("Login Successfull")
#     else:
#         print("Please invalid Detail")

# Creat_Account()
# Login()
    













