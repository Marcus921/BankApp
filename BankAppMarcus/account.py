class Account:
    def __init__(self, accountId, new_accountId, balance, add_balance):
        self.accountId = accountId
        self.new_accountId = new_accountId
        self.balance = balance
        self.add_balance = add_balance
        

    def __str__(self):
        return f"Account ID: {self.accountId}, Balance: {self.balance}, Account type: {self.accountType}"

if __name__ == "__main__":
    print("This python script is not meant to be run directly, please import in another class!")
    quit()