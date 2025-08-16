# ATM management system

class ATM:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance is: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. New balance is: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
    def display_menu(self):
        print("\n------- ATM Menu ---------\n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit \n")
        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Please select an option (1-4): \n1")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
                
# Example usage
if __name__ == "__main__":
    atm = ATM(account_number="123456789", balance=1000.00)
    atm.run()   
    
    