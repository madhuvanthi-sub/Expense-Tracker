from datetime import datetime
from multiprocessing.dummy import connection
import sqlite3
from unittest import result
DATABASE_NAME = "expenses.db"
def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    """)
    connection.commit()
    connection.close()
def add_expense(date, amount, category, description):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenses
        (date, amount, category, description)
        VALUES (?, ?, ?, ?)
    """, (date, amount, category, description))
    connection.commit()
    connection.close()
def get_expenses():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, date, amount, category, description
        FROM expenses
        ORDER BY date DESC
    """)
    expenses = cursor.fetchall()
    connection.close()
    return expenses
def delete_expense(expense_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    connection.commit()
    connection.close()
def update_expense(
    expense_id,
    date,
    amount,
    category,
    description
):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE expenses
        SET date = ?,
            amount = ?,
            category = ?,
            description = ?
        WHERE id = ?
    """, (
        date,
        amount,
        category,
        description,
        expense_id
    ))
    connection.commit()
    connection.close()
def get_monthly_total():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    current_month = datetime.now().strftime("%Y-%m")
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE substr(date, 1, 7) = ?
    """, (current_month,))
    result = cursor.fetchone()[0]
    connection.close()
    return result if result else 0