class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")

    def display_balance(self):
        print(f"💰 {self.owner}'s account balance: ${self.balance}")


# ---- Menu Interface ----
def main():
    print("🏦 Welcome to Python Bank!")

    name = input("Enter your name to open an account: ")
    account = BankAccount(name)

    while True:
        print("\n📋 Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display_balance()

        elif choice == '4':
            print("👋 Thank you for using Python Bank. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the program
main()
