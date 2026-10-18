class BankAccount:

    #initializes the class
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = float(balance)

    @property
    def get_account_number(self): #displays the account number
        return self._account_number

    @property
    def get_balance(self): #displays the account balance 
        return self._balance

    def set_account_number(self, account_number): #function that alters account number
        self.account_number = account_number

    def set_balance(self, balance): #function that alters account balance
        print(f"Update balance to: {balance}")

        if balance < 0: #if input is negative, the input is ignored
            print("The balance must not be a negative number.")

        else:
            #after checking that the input is not negative, balance is updated to match the input
            self._balance = float(balance)


a1 = BankAccount(12345, 1000) #sample values
account = 1

print(f"Account {account}")
print("Account Number: ",a1.get_account_number)
print(f"Balance: {a1.get_balance:.2f}") #:.2f formats the output so it displays 2 decimal places

print("")

#display attributes after updating balance
a1.set_balance(-100) #try to update balance with a negative number
print("Account Number: ",a1.get_account_number)
print(f"Balance: {a1.get_balance:.2f}") #:.2f formats the output so it displays 2 decimal places
