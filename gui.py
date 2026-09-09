from database import add_expense
from database import get_expenses
from database import delete_expense
from database import get_monthly_total
from charts import show_category_chart
from charts import show_monthly_chart
from export import export_expenses
from tkinter import messagebox
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
    try:
        amount = float(amount_entry.get())
    except ValueError:
        ...
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
    total_label = tk.Label(
        root,
        text="Monthly Total: ₹0",
        font=("Arial", 18, "bold")
    )
    total_label.pack(pady=10)
    def update_total():
        total = get_monthly_total()
        total_label.config(
            text=f"Monthly Total: ₹{total:.2f}"
        )
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
        load_expenses()
    add_button = tk.Button(
        root,
        text="Add Expense",
        command=save_expense
    )
    add_button.pack(pady=20)
    chart_button = tk.Button(
        root,
        text="Category Chart",
        command=show_category_chart
    )
    chart_button.pack(pady=10)
    monthly_chart_button = tk.Button(
        root,
        text="Monthly Chart",
        command=show_monthly_chart
    )
    monthly_chart_button.pack(pady=10)
    export_button = tk.Button(
        root,
        text="Export CSV",
        command=export_expenses
    )
    export_button.pack(pady=10)
    def remove_expense():
        selected = expense_table.selection()
        if not selected:
            return
        item = expense_table.item(selected[0])
        expense_id = item["values"][0]
        answer = messagebox.askyesno(
            "Delete Expense",
            "Are you sure you want to delete this expense?"
        )
        if answer:
            delete_expense(expense_id)
        load_expenses()
    delete_button = tk.Button(
        root,
        text="Delete Expense",
        command=remove_expense
    )
    delete_button.pack()
    columns = (
        "ID",
        "Date",
        "Amount",
        "Category",
        "Description"
    )
    expense_table = ttk.Treeview(
        root,
        columns=columns,
        show="headings"
    )
    for column in columns:
        expense_table.heading(
            column,
            text=column
        )
        expense_table.column(
            column,
            width=120
        )
    expense_table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )
    def load_expenses():
        for row in expense_table.get_children():
            expense_table.delete(row)
        expenses = get_expenses()
        for expense in expenses:
            expense_table.insert(
                "",
                tk.END,
                values=expense
            )
        update_total()
    load_expenses()
    root.mainloop()
if __name__ == "__main__":
    create_gui()