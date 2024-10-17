import array
import random

class Account:
    def __init__(self, account_num: int, first_name: str, last_name: str, social_security_num: str, pin: str, balance: int):
        self._account_num = account_num
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_num = social_security_num
        self._pin = pin
        self._balance = balance


    def get_account_num(self):
        return self._account_num
    
    def set_account_num(self, value):
        self._account_num = value

    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, value):
        self._first_name = value
    
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, value):
        self._last_name = value
    
    def get_social_security_num(self):
        return self._social_security_num
    
    def set_social_security_num(self, value):
        self._social_security_num = value
    
    def get_pin(self):
        return self._pin
    
    def set_pin(self, value):
        self._pin = value
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value


    def deposit(self, amount: int):
        #  method ‘deposit’ that takes one parameter - an amount to deposit into the account as a ‘long’. The method then adds the amount to the account balance and returns a ‘long’ representing the new account balance
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount: int):
        # A method ‘withdraw’ that takes one parameter - an amount to withdraw from the account as a ‘long’. The method then subtracts the amount from the account balance and returns a ‘long’ representing the new account balance
        self._balance -= amount
        return self._balance
    
    def isValidPIN(self, pin: str):
        # A method ‘isValidPIN’ that takes one parameter – A String that represents a PIN. The method then compares the PIN that was passed in against the PIN that is on the account. If the PINs match, it returns true, otherwise, it returns false
        if self._pin == pin:
            return True
        else:
            return False
        # all objects have a toString method - this indicates you are providing
        # your own version

    def __repr__(self):
        return f"""
        ===================================
        Account Number: {self._account_num}
        Owner First Name: {self._first_name}
        Owner Last Name: {self._last_name}
        Owner SSN: XXX-XX-{self._social_security_num[-4:]}
        PIN: {self._pin}
        Balance: ${self._balance}
        ===================================
        """

class Bank:
    def __init__(self):
        self.accounts = []
# =============================================================================
# CHANGE TO 100 AFTER TESTING
# =============================================================================
        self.MAX_NUM_OF_ACCOUNTS = 2
# =============================================================================
# CHANGE TO 100 AFTER TESTING
# =============================================================================

    def addAccountToBank(self, account):
        if len(self.accounts) < self.MAX_NUM_OF_ACCOUNTS:
            self.accounts.append(account)
            print("The account was successfully added.")
            return True
        else:
            print("No more accounts available.")
            return False

    def removeAccountFromBank(self, accountToRemove):
        for account in self.accounts:
            if account.get_account_num == accountToRemove.get_account_num:
                self.accounts.remove(accountToRemove)

    def findAccount(accountNumber):
        return # be sure to change this as needed
    def addMonthlyInterest(percent):
        # EXTRA CREDIT
        return

# class CoinCollector:
#     # constructor so you cannot instantiate this class
#     def __init__(self):
#         return 
#     def parseChange(coins):
#     #    implement parseChange here
#         return 0

# class BankUtility:
#     def __init__(self):
#         return
#     def promptUserForString(prompt):
#     # implement promptUserForString here
#         return "" # be sure to change this
#     def promptUserForPositiveNumber(prompt):
#     # implement promptUserForPositiveNumber here
#         return 0.0 # be sure to change this
#     def generateRandomInteger(min, max):
#     # implement generateRandomInteger here
#         return 0 # be sure to change as needed
#     def convertFromDollarsToCents(amount):
#     # implement convertFromDollarsToCents here
#         return 0 # be sure to change as needed
#     '''
#     Checks if a given string is a number (long)
#     This does NOT handle decimals.
#     YOU DO NOT NEED TO CHANGE THIS METHOD
#     THIS IS FREE FOR YOU TO USE AS NEEDED
#     @param numberToCheck String to check
#     @return true if the String is a number, false otherwise
#     '''
#     def isNumeric(numberToCheck):
#         try:
#             if numberToCheck.isdigit():
#                 return True
#             else:
#                 return False
#         except ValueError:
#             return False

# class BankManager:
#     def __init__(self):
#         return
#     # This is where you will implement your method and start
#     # the program from. The BankManager class should create an instance
#     # of a Bank object when the program runs and use that instance to
#     # manage the Accounts in the bank
#     @staticmethod
#     def promptForAccountNumberAndPIN(bank):
#     # implement promptForAccountNumberAndPIN here
#     # takes one parameter, a Bank object that represents the bank.
#     # The method should prompt the user to enter an accountnumber
#     # and then try to find a matching account with that account number
#     # in the bank.
#         return # be sure to change this as needed


test = Account(123456789, "Daniel", "Regan", "293-29-2913", "7689", 100000)
test2 = Account(123456780, "Daniel", "Regan", "293-29-2913", "7689", 100000)
test3 = Account(123456789, "Daniel", "Regan", "293-29-2913", "7689", 100000)
bank = Bank()
bank.addAccountToBank(test)
bank.addAccountToBank(test2)
print(bank.accounts)
bank.removeAccountFromBank(test2)
print(bank.accounts)
