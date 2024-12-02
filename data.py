import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self):
        self._balance = 0
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Invalid deposit amount!")
    
    def reset(self):
        self._balance = 0
        
def add_balance():
    try:
        amount = int(entry_amount.get())
        account.deposit(amount)
        label_balance.config(text=f"Balance: {account.get_balance()}")
        entry_amount.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset_balance():
    account.reset()
    label_balance.config(text=f"Balance: {account.get_balance()}")
    entry_amount.delete(0, tk.END)
    
    
root = tk.Tk()
root.title("Data Hiding in BankAccount")

account = BankAccount()

label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}")
label_balance.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

button_deposit = tk.Button(root, text="Deposit", command=add_balance)
button_deposit.pack()

button_reset = tk.Button(root, text="Reset", command=reset_balance)
button_reset.pack()

root.mainloop()