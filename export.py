import sqlite3
import csv
def export_expenses():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, date, amount, category, description
        FROM expenses
    """)
    data = cursor.fetchall()
    connection.close()
    with open(
        "expenses.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID",
            "Date",
            "Amount",
            "Category",
            "Description"
        ])
        writer.writerows(data)