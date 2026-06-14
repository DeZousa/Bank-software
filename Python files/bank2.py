class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.password = password
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print(f"✅ Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds.")
            self.history.append(f"Failed withdrawal of ${amount} (Insufficient funds)")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew ${amount}")
            print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")

    def display_balance(self):
        print(f"💰 {self.owner}'s balance: ${self.balance}")

    def show_history(self):
        print(f"📜 Transaction History for {self.owner}:")
        for entry in self.history:
            print("•", entry)


# Store all users in a dictionary: username -> BankAccount
accounts = {}

def create_account():
    username = input("Choose a username: ")
    if username in accounts:
        print("⚠️ Username already exists.")
        return
    password = input("Create a password: ")
    accounts[username] = BankAccount(username, password)
    print("✅ Account created successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    account = accounts.get(username)
    if account and account.password == password:
        print(f"✅ Welcome back, {username}!")
        user_menu(account)
    else:
        print("❌ Invalid username or password.")

def user_menu(account):
    while True:
        print("\n📋 Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Transaction History")
        print("5. Logout")

        choice = input("Choose an option (1–5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            account.show_history()
        elif choice == '5':
            print(f"👋 Logged out from {account.owner}'s account.")
            break
        else:
            print("⚠️ Invalid choice.")

def main():
    while True:
        print("\n🏦 Python Bank Main Menu")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1–3): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("👋 Thanks for visiting Python Bank. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

# Run the program
main()
