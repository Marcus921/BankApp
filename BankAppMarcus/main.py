import bank

bank = bank.Bank()

def main():
    print("Welcome to Marcus Bank")
    first_name, last_name, SSN_list, accId, balance, newAcc, add_balance = read_file()
    option = 0
    while option != 11:

        # displaying option menu
        banking_menu = ["1.  Open Account", "2.  Modify Account", "3.  Close Account with Account Number", "4.  Close Account with SSN_list", "5.  Withdraw Money",
                        "6.  Deposit Money", "7.  Add Account", "8.  Deposit To Other Account", "9.  Withdraw From Other Account", "10. Show Accounts", "11. Save & Quit"]

        for option in banking_menu:
            print(option)
        user_input = False

       # validation for user input
        while not user_input:
            try:
                option = int(input("Please enter an option: "))
                if 0 < option < 12:
                    user_input = True
                else:
                    print("\nPlease enter a number greater than 0 and less than 12\n")
                    for option in banking_menu:
                        print(option)
            except:
                print("\nError -- Please enter a number between 1 to 11 only\n")
                for option in banking_menu:
                    print(option)

# if statement for all of the options
        if option == 1:
            bank.open_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 2:
            bank.ch_name(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 3:
            bank.shutdown_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 4:
            bank.shutdown_ssn_list(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 5:
            bank.cash_out(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)    

        elif option == 6:
            bank.add_money(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 7:
            bank.add_acc(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 8:
            bank.add_bal(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 9:
            bank.money_out(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 10:
            bank.report(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

        elif option == 11:
            bank.exit(first_name, last_name, SSN_list, accId, balance, newAcc, add_balance)

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

if __name__ == "__main__":
    main()