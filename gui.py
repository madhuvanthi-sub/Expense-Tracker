from database import add_expense
import tkinter as tk
from tkinter import ttk
def create_gui():
    root = tk.Tk()
    root.title("Expense Tracker")
    root.geometry("900x600")
    title = tk.Label(
        root,
        text="Expense Tracker",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)
    date_label = tk.Label(root, text="Date")
    date_label.pack()
    date_entry = tk.Entry(root)
    date_entry.pack()
    amount_label = tk.Label(root, text="Amount")
    amount_label.pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    category_label = tk.Label(root, text="Category")
    category_label.pack()
    category_combo = ttk.Combobox(
        root,
        values=[
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Entertainment",
            "Health",
            "Education",
            "Other"
        ]
    )
    category_combo.pack()
    description_label = tk.Label(
        root,
        text="Description"
    )
    description_label.pack()
    description_entry = tk.Entry(root)
    description_entry.pack()
    def save_expense():
        date = date_entry.get()
        amount = amount_entry.get()
        category = category_combo.get()
        description = description_entry.get()
        add_expense(
            date,
            float(amount),
            category,
            description
        )
        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        category_combo.set("")
        root.mainloop()
    add_button = tk.Button(
        root,
        text="Add Expense",
        command=save_expense
    )
    add_button.pack(pady=20)
    root.mainloop()
if __name__ == "__main__":
    create_gui()