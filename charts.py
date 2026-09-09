import sqlite3
import matplotlib.pyplot as plt
def show_category_chart():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)
    data = cursor.fetchall()
    connection.close()
    if not data:
        return
    categories = []
    amounts = []
    for category, amount in data:
        categories.append(category)
        amounts.append(amount)
    plt.figure(figsize=(7, 7))
    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )
    plt.title("Expenses by Category")
    plt.show()
def show_monthly_chart():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT substr(date, 1, 7), SUM(amount)
        FROM expenses
        GROUP BY substr(date, 1, 7)
        ORDER BY substr(date, 1, 7)
    """)
    data = cursor.fetchall()
    connection.close()
    if not data:
        return
    months = []
    amounts = []
    for month, amount in data:
        months.append(month)
        amounts.append(amount)
    plt.figure(figsize=(8, 5))
    plt.bar(months, amounts)
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.title("Monthly Expenses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()