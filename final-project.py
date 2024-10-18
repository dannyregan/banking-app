import math
import random


class Account:
    def __init__(self, account_num: int, first_name: str, last_name: str, social_security_num: str, pin: str, balance: int = 0):
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

    def toString(self):
        return f"""
        ===================================
        Account Number: {self._account_num}
        Owner First Name: {self._first_name}
        Owner Last Name: {self._last_name}
        Owner SSN: XXX-XX-{self._social_security_num[-4:]}
        PIN: {self._pin}
        Balance: ${self._balance / 100:.2f}
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
            print(account.toString())
            print("The account was successfully added.")
            return True
        else:
            print("No more accounts available.")
            return False

    def removeAccountFromBank(self, accountToRemove):
        for account in self.accounts:
            if account.get_account_num == accountToRemove.get_account_num:
                self.accounts.remove(accountToRemove)

    def findAccount(self, accountNumber):
        for account in self.accounts:
            if account.get_account_num() == accountNumber:
                return account
        return None

    def addMonthlyInterest(percent):
# =================================================
# EXTRA CREDIT
# =================================================
        return

    def checkAccountNum(self, accountNum):
        for account in self.accounts:
            if account.get_account_num() == accountNum:
                return True
            return False


class CoinCollector:
    # constructor so you cannot instantiate this class
    def __init__(self):
        return 

    def parseChange(self, coins):
        total = 0
        coins = coins.upper()
        coins = list(coins)
        for coin in coins:
            if coin == 'P':
                total += 1
            if coin == 'N':
                total += 5
            if coin == 'D':
                total += 10
            if coin == 'Q':
                total += 25
            if coin == 'H':
                total += 50
            if coin == 'W':
                total += 100
        return total

class BankUtility:
    def __init__(self):
        return

    def promptUserForString(self, prompt):
        response = input(prompt)
        return f'{response}'

    def promptUserForPositiveNumber(self, prompt):
        while True:
            response = input(prompt)
            try:
                if float(response) > 0:
                    return response
                if float(response) <= 0:
                    print("Amount cannot be 0 or negative. Try again.")
            except:
                print('Please enter a number.')

    def generateRandomInteger(self, min, max):
        return random.randint(min, max)

    def convertFromDollarsToCents(self, amount):
        cents = round(amount * 100)
        return cents

    def numOfBills(self, amount, bill):
        numOfBills = math.floor(amount / bill)
        return numOfBills
    '''
    Checks if a given string is a number (long)
    This does NOT handle decimals.
    YOU DO NOT NEED TO CHANGE THIS METHOD
    THIS IS FREE FOR YOU TO USE AS NEEDED
    @param numberToCheck String to check
    @return true if the String is a number, false otherwise
    '''
    def isNumeric(self, numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

class BankManager:
    def __init__(self):
        self.bank = Bank()
    
    def main(self):
        while True:
            print("======================================")
            print("What do you want to do?")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")
            print("======================================")

            selection = input("Select an option: ")

            if selection == '1':
                print("OPEN ACCOUNT")
                firstName = input("Enter Account Owner's Fist Name: ")
                lastName = input("Enter Account Owner's Last Name: ")
                ssn = input("Enter Account Owner's SSN (9 digits): ")
                pin = BankUtility().generateRandomInteger(0,999)
                pin = f"{pin:04d}"

                accountNumCheck = True
                while accountNumCheck:
                    accountNum = BankUtility().generateRandomInteger(10000000,99999999)
                    accountNumCheck = self.bank.checkAccountNum(accountNum)

                account = Account(accountNum, firstName, lastName, ssn, pin)
                self.bank.addAccountToBank(account)

            elif selection == '2':
                account = self.promptForAccountNumberAndPIN(self.bank)
                if account:
                    print(account.toString())

            elif selection == '3':
                account = self.promptForAccountNumberAndPIN(self.bank)
                if account:
                    pin = input("Enter new PIN: ")
                    if len(pin) == 4:
                        pinCheck = input("Enter new PIN again to confirm: ")
                        if pin == pinCheck:
                            account.set_pin(pin)
                            print("PIN updated")
                    else: print("PIN must be four digits long")

            elif selection == '4':
                account = self.promptForAccountNumberAndPIN(self.bank)
                if account:
                    amount = BankUtility().promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
                    account.deposit(float(amount))
                    print(f"New balance: {account.get_balance():.2f}")

            elif selection == '5':
                print("Account to transfer from:")
                accountFrom = self.promptForAccountNumberAndPIN(self.bank)
                if accountFrom:
                    print("Account to transfer to:")
                    accountTo = self.promptForAccountNumberAndPIN(self.bank)
                    if accountTo:
                        amount = BankUtility().promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
                        accountFrom.withdraw(float(amount))
                        accountTo.deposit(float(amount))
                        print("Transfer Complete")
                        print(f"New balance in account {accountTo.get_account_num()}: ${accountFrom.get_balance():.2f}")
                        print(f"New balance in account {accountTo.get_account_num()}: ${accountTo.get_balance():.2f}")
                    
            elif selection == '6':
                account = self.promptForAccountNumberAndPIN(self.bank)
                if account:
                    amount = BankUtility().promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
                    account.withdraw(float(amount))
                    print(f"New balance: ${account.get_balance():.2f}")

            elif selection == '7':
                account = self.promptForAccountNumberAndPIN(self.bank)
                if account:
                    amount = float(BankUtility().promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): "))
                    if amount % 5 == 0:
                        if 5 <= amount <= 1000:
                            account.withdraw(amount)
                            twenties = BankUtility().numOfBills(amount, 20)
                            amount -= twenties * 20
                            tens = BankUtility().numOfBills(amount, 10)
                            amount -= tens * 10
                            fives = BankUtility().numOfBills(amount, 5)
                            print(f"Number of 20-dollar bills: {twenties}")
                            print(f"Number of 10-dollar bills: {tens}")
                            print(f"Number of 5-dollar bills: {fives}")
                            print(f"New balance: ${account.get_balance():.2f}")
                        else:
                            print("Invalid amount. Try again.")
                    else:
                        print("Invalid amount. Try again.")


                    


            elif selection == '11':
                break
            else:
                print("Invalid selection.")

    def promptForAccountNumberAndPIN(self, bank):
        accountNum = input("Enter an account number: ")
        for account in bank.accounts:
            # print(str(account.get_account_num()))
            if str(account.get_account_num()) == accountNum:
                pin = input("Input PIN: ")
                if account.isValidPIN(pin):
                    return account
                # if pin == account.get_pin():
                #     return account
                else:
                    print("Invalid PIN")
                    return False
        print(f"Account not found for account number: {accountNum}")
        return None



    # @staticmethod
    # def promptForAccountNumberAndPIN(bank):
    # # implement promptForAccountNumberAndPIN here
    # # takes one parameter, a Bank object that represents the bank.
    # # The method should prompt the user to enter an accountnumber
    # # and then try to find a matching account with that account number
    # # in the bank.
    #     return # be sure to change this as needed


bankManager = BankManager()
bankManager.main()

