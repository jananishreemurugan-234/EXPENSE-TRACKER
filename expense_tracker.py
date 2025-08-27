import json
import os
import matplotlib.pyplot as plt

FILE_NAME = "data.json"

# ---------- File Handling ----------
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as f:
        json.dump(expenses, f, indent=4)

# ---------- Expense Functions ----------
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    expenses = load_expenses()
    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully!")

def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()
    monthly_expenses = [e for e in expenses if e["date"].startswith(month)]

    summary = {}
    for e in monthly_expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\nMonthly Expense Report:")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

    return summary

# ---------- Chart Functions ----------
def plot_chart(summary):
    if not summary:
        print("No expenses to show for this month!")
        return

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%', startangle=90)
    plt.title("Expense Distribution (Pie Chart)")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(6, 4))
    plt.bar(summary.keys(), summary.values(), color='skyblue')
    plt.xlabel("Categories")
    plt.ylabel("Amount (₹)")
    plt.title("Expenses by Category (Bar Chart)")
    plt.show()

# ---------- Main Menu ----------
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Monthly Report & Charts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            summary = monthly_report()
            plot_chart(summary)
        elif choice == '3':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()