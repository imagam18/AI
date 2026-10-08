# ATM Machine Software

class ATM:

    def __init__(self,balance, pin):
        self.balance = balance
        self.pin = pin

        print("Welcome to ATM")
        

    

    def create_pin(self):

        self.pin = input("Enter your PIN: ")

        print("✅ PIN created successfully.")

        

    def deposit(self,deposit_amount=None):

        if self.pin == "":
            print(" Please create a PIN first.")
            
            return

        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:

            if deposit_amount is None:
                amount = float(input("Enter amount to deposit: "))
            else:
                amount = deposit_amount

            if amount > 0:
                self.balance += amount

                print(f"Deposited: ₹{amount}")
                print(f"New balance: ₹{self.balance}")

            else:
                print(" Amount must be greater than 0.")

        else:
            print(" Incorrect PIN!")

        

    def withdraw(self,withdraw_amount=None):

        if self.pin == "":
            print("Please create a PIN first.")
            
            return

        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:

            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print(" Amount must be greater than 0.")

            elif amount <= self.balance:

                self.balance -= amount

                print(f"Withdrawn: ₹{amount}")
                print(f"Remaining balance: ₹{self.balance}")

            else:
                print(" Insufficient balance!")

        else:
            print(" Incorrect PIN!")

        

    def check_balance(self):

        if self.pin == "":
            print(" Please create a PIN first.")
            
            return

        user_pin = input("Enter your PIN: ")

        if user_pin == self.pin:

            print(f"Your balance is: ₹{self.balance}")

        else:
            print("Incorrect PIN!")

        

    def exit(self):

        print("Thank you for using ATM!")
        exit()


# Create ATM object
person1 = ATM(balance=1000, pin="1234")
person1.deposit(500)
person1.withdraw(200)