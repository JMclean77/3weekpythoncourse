"""
This is a class for a bank account. The class includes 4 methods that allow the user to
deposit, withdrawl, agree to a bank fee, and display their account details.
"""

class BankAccount():
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_nl;umber)
        self.name = name
        self.balance = float(balance)

    def deposit(self):
        """
             This function allows a user to deposit into their bank account and does error checking to
             ensure they are entering a number and not providing invalid input
             """
        try:
            amount= float(input("Enter amount to deposit: \n"))
            if amount == float(amount):
                self.balance += amount
                print(f"Deposit Successful, new balance is: {self.balance}\n")
        except ValueError:
            print("Deposit failed, please try again\n")

    def withdrawl(self):
        """
           This is a method that allows a user to make a withdrawl from a bank account and does error checking to
           ensure they are entering a number and not providing invalid input as well as checking if they have sufficient
           funds in their account to conduct the withdrawl
           """
        try:
            amount= float(input("Enter amount to withdrawl: \n"))
            if amount == float(amount):
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawl Successful, new balance is: {self.balance}\n")
                else:
                    print("Withdrawl failed, Insufficient balance\n")
        except ValueError:
            print("Withdrawl failed, Need a valid amount\n")

    def bank_fees(self):
        """
        This is a method that prompts the user to agree to a bank fee to be applied to their balance.
        this then deducts 5% from their balance and then updates the balance accordingly
        """
        choice= input("Would you like to apply your bank fee of 5%? (yes/no) \n").lower()
        if choice == "yes":
            fee= self.balance * 0.05
            self.balance -= fee
            print(f"Bank Fees Successful, new balance is: {self.balance}\n")
        elif choice == "no":
            print("You did not pay your bank fees.\n")
        else:
            print("Invalid choice, must be yes or no\n")

    def display(self):
        """
        This is a method that allows the user to display their account details.
        """
        print("The account holdername: ",self.name)
        print("The account holder account number: ",self.account_number)
        print("The account holders balance: ",self.balance)


#Sample data to show the use of the methods and class
jaisen_bank= BankAccount(198160, "Jaisen", 1000)
jaisen_bank.deposit()
jaisen_bank.withdrawl()
jaisen_bank.bank_fees()
jaisen_bank.display()



