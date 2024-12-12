import getpass

class Account:
    def __init__(self, account_number, account_type, pin, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"${amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")
        return f"${amount} withdrawn successfully."

    def get_transaction_history(self):
        if not self.transaction_history:
            return "No transactions found."
        return "\n".join(self.transaction_history)

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_type, pin):
        if account_number in self.accounts:
            return "Account already exists."
        self.accounts[account_number] = Account(account_number, account_type, pin)
        return "Account created successfully."

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if not account or account.pin != pin:
            return None
        return account

    def run(self):
        while True:
            print("\nWelcome to the ATM Simulator")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                account_number = input("Enter account number: ")
                account_type = input("Enter account type (savings/current): ")
                pin = getpass.getpass("Set a 4-digit PIN: ")
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN format. Must be 4 digits.")
                    continue
                print(self.create_account(account_number, account_type, pin))

            elif choice == "2":
                account_number = input("Enter account number: ")
                pin = getpass.getpass("Enter your PIN: ")
                account = self.authenticate(account_number, pin)
                if not account:
                    print("Authentication failed. Invalid account number or PIN.")
                    continue

                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. View Transaction History")
                    print("5. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        print(f"Your balance is: ${account.check_balance()}")

                    elif user_choice == "2":
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            print(account.deposit(amount))
                        except ValueError:
                            print("Invalid input. Please enter a valid amount.")

                    elif user_choice == "3":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            print(account.withdraw(amount))
                        except ValueError:
                            print("Invalid input. Please enter a valid amount.")

                    elif user_choice == "4":
                        print("Transaction History:")
                        print(account.get_transaction_history())

                    elif user_choice == "5":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "3":
                print("Thank you for using the ATM Simulator. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
