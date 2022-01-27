import random
from bank import *
from account import *
from customer import *


def main():
    print("Welcome to Marcus Bank")
    first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = read_file()
    option = 0
    while option != 9:

        # displaying option menu
        banking_menu = ["1. Open Account", "2. Modify Account", "3. Close Account with Account Number", "4. Close Account with SSN_list", "5. Withdraw Money",
                        "6. Deposit Money", "7. Add Account(Under Construction)", "8. Show Accounts", "9. Save & Quit"]

        for option in banking_menu:
            print(option)
        user_input = False

       # validation for user input
        while not user_input:
            try:
                option = int(input("Please enter an option: "))
                if 0 < option < 10:
                    user_input = True
                else:
                    print("\nPlease enter a number greater than 0 and less than 10\n")
                    for option in banking_menu:
                        print(option)
            except:
                print("\nError -- Please enter a number between 1 to 9 only\n")
                for option in banking_menu:
                    print(option)

# if statement for all of the options
        if option == 1:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = open_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 2:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance  = ch_name(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 3:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = shutdown_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 4:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = shutdown_ssn_list(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 5:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = cash_out(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)    

        elif option == 6:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = add_money(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 7:
            first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = add_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 8:
            report(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 9:
            exit(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)
   


# Functions for all of the switch statement
def read_file():
    first_name = []
    last_name = []
    SSN_list = []
    accId = []
    balance = []
    newAcc = []
    add_balance = []

# reading the text file
    f = open("bank.txt", "r")
    lines = f.readlines()
    for line in lines:
        information = line.split()
        accId.append(information[0])
        SSN_list.append(information[1])
        first_name.append(information[2])
        last_name.append(information[3])
        balance.append(float(information[4]))
        newAcc.append(information[7])
        add_balance.append(float(information[8]))
    return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance


# Function for opening an account
def open_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
        fname = input("Please enter your first name: ")
        first_name.append(fname)
        lname = input("Please enter your last name: ")
        last_name.append(lname)
        newAcc.append("Placeholder")
        add_balance.append(0.0)
        SSN = input("Please enter your SSN: ")
        if SSN in SSN_list:
            print("You already have an account")
            return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance
        else:
            SSN_list.append(SSN)  
            number = str(random.randint(1000, 1000000))
            print("Account created with name:",fname, lname,"SSN:", SSN,"with the account number:", number)
            accId.append(number)
            balance.append(0.0) 
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance

# Function for adding an account
def add_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):  
    s_number = input("Please enter your SSN: ")
    index = 0
    found = False
    for s in SSN_list:
        if s in s_number:
            found = True
            break
        index = index + 1
    if found:
        number = str(random.randint(1000, 1000000))
        newAcc[index] = number
        print("New account was opened with ID: ", number)
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance
    else:
        print("Sorry, that SSN does not exist")
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance

# Modify Account
def ch_name(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    p_number=input("\nEnter you're SSN: ")
    index = 0
    found = False
    for p in SSN_list:
        if p == p_number:
            found = True
            break
        index = index + 1
    if found:
        fname = input("Enter new first name: ")
        first_name[index] = fname
        lname = input("Enter new last name: ")
        last_name[index] = lname
        print("Your new name is",fname,lname)
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance
    else:
        print("No such SSN")
        return first_name, last_name, SSN_list, accId, balance, add_balance

# Function for closing an account with SSN
def shutdown_ssn_list(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    social_security_number = input("\nEnter your SSN:\n")
    index = 0
    found = False
    for s in SSN_list:
        if s == social_security_number:
            found = True
            break
        index = index + 1
    if found:
        print("\nSorry to see you go ", first_name[index], last_name[index], "Your remaining balance", balance[index], "will be withdrawn" "\n")
        # deletes the 6 lists from their index position.
        del accId[index]
        del balance[index]
        del first_name[index]
        del last_name[index]
        del SSN_list[index]
        del newAcc[index]
        del add_balance[index]

    else:
        print("\nError -- No account exists under the number you provided\n")
    return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance


# Function for closing an account with account number
def shutdown_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in accId:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        print("\nSorry to see you go", first_name[index], last_name[index], "Your remaining balance", balance[index], "will be withdrawn" "\n")
        # deletes the 6 lists from their index position.
        del accId[index]
        del balance[index]
        del first_name[index]
        del last_name[index]
        del SSN_list[index]
        del newAcc[index]
        del add_balance[index]

    else:
        print("\nError -- No account exists under the number you provided\n")
    return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance


# Function for Withdrawing money from an account
def cash_out(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in accId:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                withdraw_amount = float(input("Enter the amount you want to withdraw: "))
                # The Amount is the new amount the customer has withdrawn
                if withdraw_amount < 0:  # if not a positive int print message and ask for input again
                    print("ERROR -- input must be a positive integer, try again")
                    break
                amount = balance[index] - withdraw_amount
                # if the amount is greater than or = 0 it will take the amount away from the balance list.
                if amount > 0:
                    balance[index] = balance[index] - withdraw_amount
                    print("An amount of ", "$", format(withdraw_amount, ".2f"), " is removed from your account ",
                          account_number,
                          sep="")
                    print("Your current balance is ", "$", format(balance[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Unfortunately you don't have a sufficient funds",
                          first_name[index])
                    print("Your balance after your current transaction is ", "$",
                          format(balance[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance
    else:
        print("\n Sorry that account number does not exist \n")
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance


# Function for depositing an amount to an account
def add_money(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    account_number = input("\nEnter your account number:\n")
    index = 0
    found = False
    for i in accId:
        if i == account_number:
            found = True
            break
        index = index + 1
    if found:
        problem = True
        while problem:
            try:
                deposit_amount = float(input("Enter the amount you want to deposit: "))
                # The Amount of customer chooses to deposit
                if deposit_amount < 0:  # if not a positive int print message and ask for input again
                    print("ERROR -- input must be a positive integer, try again")
                    break
                amount = balance[index] + deposit_amount
                # if the amount is greater than or = 0 it will added to the balance list.
                if amount > 0:
                    balance[index] = balance[index] + deposit_amount
                    print("An amount of ", "$", format(deposit_amount, ".2f"), " is added from your account ",
                          account_number,
                          sep="")
                    print("Your current balance is ", "$", format(balance[index], ".2f"), sep="")
                    print("")
                    problem = False
                else:
                    print("Error -- Please enter a positive number",
                          first_name[index])
                    print("Your balance after your current transaction is ", "$",
                          format(balance[index], ".2f"), sep="")
                    print("")
                    break
            finally:
                return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance
    else:
        print("\n Sorry that account number does not exist \n")
        return first_name, last_name, SSN_list, accId, balance, newAcc, add_balance


# Function to show all the accounts with details
def report(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    for i in range(len(accId)):
        print("\nFull name:", first_name[i], last_name[i], "SSN:", SSN_list[i], "Account number:", accId[i], "Balance: $", balance[i], "Account type: Debit",newAcc[i], add_balance[i])
        

def exit(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance):
    print("Thank You For Using Marcus Bank")
    quit_file = open("bank.txt", "w")
    for i in range(len(accId)):
        save = accId[i] + " " + SSN_list[i] + " " + first_name[i] + " " + last_name[i] + " " + str(balance[i]) + " Debit " + "# " + newAcc[i] + " " + str(add_balance[i]) + "\n"
        quit_file.write(save)
    quit_file.close()


main()