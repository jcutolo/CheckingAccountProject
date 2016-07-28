class People():
    
    def __init__(self):
        self.listOfPeople = list()
        
    def addPerson(self, person):
        self.listOfPeople.append(person)
    
    def showList(self):
        for person in self.listOfPeople:
            print(person.name)
            
class Person():
    
    def __init__(self, name, startUp):
        self.name = name
        self.startUp = startUp
        self.checking = CheckingAccount(name, startUp)
        self.savings = SavingsAccount(name)
    
class CheckingAccount():
    
    def __init__(self, name, startUp):
        self.name = name
        self.checkingBalance = startUp
    
    def deposit_Checking(self, amount):
        self.checkingBalance += amount
    
    def withdrawal_Checking(self, amount):
        if self.checkingBalance < amount:
            print("Insufficient funds for this transaction!")
        else:
            self.checkingBalance -= amount

    def checkBalance_Checking(self):
        print(self.checkingBalance)
    
    def transfer_Savings(self, amount, otherAccount):
        if self.checkingBalance < amount:
            raise ValueError("Insufficient Funds!")
        self.checkingBalance -= amount
        otherAccount.deposit_Savings(amount)
    
class SavingsAccount():
    
    def __init__(self, name):
        self.name = name
        self.savingsBalance = 0
        
    def deposit_Savings(self, amount):
        self.savingsBalance += amount
    
    def checkBalance_Savings(self):
        print(self.savingsBalance)
    
    def transfer_Checking(self, amount, otherAccount):
        if self.savingsBalance < amount:
            raise ValueError("Insufficient Funds!")
        self.savingsBalance -= amount
        otherAccount.deposit_Checking(amount)
        

    
class Simulator():
    
    def __init__(self):
        self.interface = None
    
    def userInterface(self):
        print("-----Hello! Welcome to the Bank!-----")
        _name = raw_input("What is your name? ")
        _startUp = int(raw_input("How much money do you want to start your account with? "))
        print("Hello " + _name + ". You elected to start your account with " + str(_startUp) + "$.\n")
        print("Your brand new checking and savings accounts will now be created for you! Congratulations!")
        print("Please note that your savings account will start at a balance of zero and will remain that way")
        print("until you decide to transfer money to it!")
        person = Person(_name, _startUp)
        end = False
        while(not end):
            choice = int(raw_input("Please select an account to begin your transaction.\n1. Checking\n2. Savings\n3. Quit\n--> "))
            if choice == 1:
                user_choice = int(raw_input("Choose a transaction type!\n1. Deposit\n2. Withdrawal\n3. Transfer\n4. Balance\n--> "))
                if int(user_choice) == 1:
                    deposit_amount = int(raw_input("How much money would you like to deposit? "))
                    print("Depositing " + str(deposit_amount) + ".")
                    person.checking.deposit_Checking(deposit_amount)
                elif int(user_choice) == 2:
                    withdrawal_amount = int(raw_input("How much money would you like to withdrawal? "))
                    print("Withdrawing " + str(withdrawal_amount) + ".")
                    person.checking.withdrawal_Checking(withdrawal_amount)
                elif int(user_choice) == 3:
                    transfer_amount = int(raw_input("How much money would you like to transfer between your accounts? "))
                    print("Transferring " + str(transfer_amount) + ".")
                    person.checking.transfer_Savings(transfer_amount, person.savings)
                elif int(user_choice) == 4:
                    c_balance = person.checking.checkBalance_Checking()
                    print(c_balance)
                else:
                    print("Not a valid choice! Try again!")
            elif int(choice) == 2:
                user_choice = int(raw_input("Choose a transaction type!\n1. Deposit\n2. Transfer\n3. Balance\n--> "))
                if int(user_choice) == 1:
                    deposit_amount = int(raw_input("How much money would you like to deposit? "))
                    print("Depositing " + str(deposit_amount) + ".")
                    person.savings.deposit_Savings(deposit_amount)
                elif int(user_choice) == 2:
                    transfer_amount = int(raw_input("How much money would you like to transfer between your accounts? "))
                    print("Transferring " + str(transfer_amount) + ".")
                    person.savings.transfer_Checking(transfer_amount, person.checking)
                elif int(user_choice) == 3:
                    person.savings.checkBalance_Savings()
                else:
                    print("Not a valid choice! Try again!")
            elif int(choice) == 3:
                print("Thank you for using the bank today! Have a great day!")
                end = True
            else:
                print("Not a valid choice! Try again!")

if __name__ == '__main__':
      
    simulation = Simulator()
    simulation.userInterface()
           
