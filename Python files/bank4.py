import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "accounts.json"

# --- BankAccount class ---
class BankAccount:
    def __init__(self, owner, password, balance=0, history=None):
        self.owner = owner
        self.password = password
        self.balance = balance
        self.history = history or []

    def to_dict(self):
        return {
            "owner": self.owner,
            "password": self.password,
            "balance": self.balance,
            "history": self.history
        }

# --- Load & Save Functions ---
def load_accounts():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
        return {
            username: BankAccount(**info)
            for username, info in data.items()
        }

def save_accounts():
    with open(FILE_NAME, "w") as file:
        data = {
            username: acc.to_dict()
            for username, acc in accounts.items()
        }
        json.dump(data, file, indent=4)

accounts = load_accounts()

# --- GUI Application ---
class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Python Bank Login")
        master.geometry("300x250")
        master.resizable(False, False)

        self.label = tk.Label(master, text="🏦 Welcome to Python Bank", font=("Arial", 14))
        self.label.pack(pady=10)

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", width=10, command=self.login)
        self.login_button.pack(pady=5)

        self.signup_button = tk.Button(master, text="Sign Up", width=10, command=self.signup)
        self.signup_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        account = accounts.get(username)
        if account and account.password == password:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.open_account_window(account)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in accounts:
            messagebox.showerror("Error", "Username already exists.")
            return
        accounts[username] = BankAccount(username, password)
        save_accounts()
        messagebox.showinfo("Success", "Account created successfully!")

    def open_account_window(self, account):
        top = tk.Toplevel()
        top.title(f"{account.owner}'s Account")
        top.geometry("300x300")

        balance_label = tk.Label(top, text=f"Balance: ${account.balance}", font=("Arial", 12))
        balance_label.pack(pady=10)

        def deposit():
            amount = simple_prompt("Enter amount to deposit:")
            if amount:
                try:
                    amt = float(amount)
                    account.balance += amt
                    account.history.append(f"Deposited ${amt}")
                    save_accounts()
                    balance_label.config(text=f"Balance: ${account.balance}")
                except:
                    messagebox.showerror("Error", "Invalid amount.")

        def withdraw():
            amount = simple_prompt("Enter amount to withdraw:")
            if amount:
                try:
                    amt = float(amount)
                    if amt > account.balance:
                        messagebox.showerror("Error", "Insufficient funds.")
                        account.history.append(f"Failed withdrawal of ${amt}")
                    else:
                        account.balance -= amt
                        account.history.append(f"Withdrew ${amt}")
                        save_accounts()
                        balance_label.config(text=f"Balance: ${account.balance}")
                except:
                    messagebox.showerror("Error", "Invalid amount.")

        def show_history():
            history_win = tk.Toplevel(top)
            history_win.title("Transaction History")
            tk.Label(history_win, text="Transaction History:").pack()
            for item in account.history:
                tk.Label(history_win, text="• " + item).pack(anchor='w')

        tk.Button(top, text="Deposit", width=20, command=deposit).pack(pady=5)
        tk.Button(top, text="Withdraw", width=20, command=withdraw).pack(pady=5)
        tk.Button(top, text="Show History", width=20, command=show_history).pack(pady=5)
        tk.Button(top, text="Logout", width=20, command=top.destroy).pack(pady=5)

def simple_prompt(prompt_text):
    popup = tk.Toplevel()
    popup.geometry("250x120")
    popup.title("Input")

    label = tk.Label(popup, text=prompt_text)
    label.pack(pady=5)

    entry = tk.Entry(popup)
    entry.pack()

    result = {}

    def submit():
        result['value'] = entry.get()
        popup.destroy()

    tk.Button(popup, text="OK", command=submit).pack(pady=5)
    popup.wait_window()
    return result.get('value')

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
