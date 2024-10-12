import random

class Account:
    def __init__(self, account_num, first_name, last_name, social_security_num, pin, balance):
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
        
    # add your attributes here
    # add methods as getters and setters for attributes
    def deposit(amount):
        # implement deposit here
        return 0
    def withdraw(amount):
        # implement withdraw here
        return 0 # be sure to change this
    def isValidPIN(pin):
        # implement isValidPIN here
        return False # be sure to change this
        # all objects have a toString method - this indicates you are providing
        # your own version
    def __repr__(self):
        return "" # change this as needed

class Bank:
    def addAccountToBank(account):
        # implement addAccountToBank here
        return False; # be sure to change this as needed
    def removeAccountFromBank(account):
        # implement removeAccountFromBank here
        return False; # be sure to change this as needed
    def findAccount(accountNumber):
        return # be sure to change this as needed
    def addMonthlyInterest(percent):
        # EXTRA CREDIT
        return

class CoinCollector:
    # constructor so you cannot instantiate this class
    def __init__(self):
        return 
    def parseChange(coins):
    #    implement parseChange here
        return 0

class BankUtility:
    def __init__(self):
        return
    def promptUserForString(prompt):
    # implement promptUserForString here
        return "" # be sure to change this
    def promptUserForPositiveNumber(prompt):
    # implement promptUserForPositiveNumber here
        return 0.0 # be sure to change this
    def generateRandomInteger(min, max):
    # implement generateRandomInteger here
        return 0 # be sure to change as needed
    def convertFromDollarsToCents(amount):
    # implement convertFromDollarsToCents here
        return 0 # be sure to change as needed
    '''
    Checks if a given string is a number (long)
    This does NOT handle decimals.
    YOU DO NOT NEED TO CHANGE THIS METHOD
    THIS IS FREE FOR YOU TO USE AS NEEDED
    @param numberToCheck String to check
    @return true if the String is a number, false otherwise
    '''
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

class BankManager:
    def __init__(self):
        return
    # This is where you will implement your method and start
    # the program from. The BankManager class should create an instance
    # of a Bank object when the program runs and use that instance to
    # manage the Accounts in the bank
    @staticmethod
    def promptForAccountNumberAndPIN(bank):
    # implement promptForAccountNumberAndPIN here
    # takes one parameter, a Bank object that represents the bank.
    # The method should prompt the user to enter an accountnumber
    # and then try to find a matching account with that account number
    # in the bank.
        return # be sure to change this as needed
