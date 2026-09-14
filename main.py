DATA_FILE = "bank_data.txt"


def load_data():
    try:
        file = open(DATA_FILE, "r")

        lines = file.readlines()

        file.close()

        name = lines[0].strip()
        balance = float(lines[1].strip())

        expenses = []

        for line in lines[2:]:
            description, category, amount = line.strip().split("|")

            expenses.append({
                "description": description,
                "category": category,
                "amount": float(amount)
            })

        return name, balance, expenses

    except FileNotFoundError:
        return None, 0, []

    except Exception as error:
        print("Error loading data:", error)
        return None, 0, []


def save_data(name, balance, expenses):
    try:
        with open(DATA_FILE, "w") as file:
            file.write(name + "\n")
            file.write(str(balance) + "\n")

            for expense in expenses:
                file.write(
                    f"{expense['description']}|"
                    f"{expense['category']}|"
                    f"{expense['amount']}\n"
                )

        print("Data saved successfully.")

    except Exception as error:
        print("Error saving data:", error)


def create_account():
    print("\n===== CREATE ACCOUNT =====")
    name = input("Enter your name: ")
    while True:
        try:
            balance = float(input("Enter starting balance: ■"))
            if balance < 0:
                print("Balance cannot be negative.")
                continue
            return name, balance
        except ValueError:
            print("Please enter a valid amount.")


def check_balance(balance):
 print(f"\nCurrent Balance: ■{balance:,.2f}")


def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: ■"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance
        balance += amount
        print(f"■{amount:,.2f} deposited successfully.")
    except ValueError:
        print("Invalid amount.")


def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: ■"))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"■{amount:,.2f} withdrawn successfully.")
    except ValueError:
        print("Invalid amount.")
        return balance  


def add_expense(expenses, balance):
    try:
        description = input("Expense description: ")
        category = input("Category: ")
        amount = float(input("Amount: ₦"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance

        if amount > balance:
            print("Not enough balance.")
            return balance

        expense = {
            "description": description,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        balance -= amount

        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount.")

    return balance

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return
    print("\n===== ALL EXPENSES =====")
    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Description : {expense['description']}")
        print(f"Category : {expense['category']}")
        print(f"Amount : ■{expense['amount']:,.2f}")


def search_expense(expenses):

    keyword = input("Enter expense name to search: ").lower()

    found = False

    for expense in expenses:

        if keyword in expense["description"].lower():

            print("\nExpense Found")
            print(f"Description : {expense['description']}")
            print(f"Category : {expense['category']}")
            print(f"Amount : ₦{expense['amount']:,.2f}")

            found = True

    if not found:
        print("Expense not found.")


def expense_summary(expenses):

    if not expenses:
        print("No expenses available.")
        return

    summary = {}

    for expense in expenses:

        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]

        else:
            summary[category] = expense["amount"]

    print("\n===== EXPENSE SUMMARY =====")

    total = 0

    for category, amount in summary.items():

        print(f"{category}: ₦{amount:,.2f}")

        total += amount

    print(f"\nTotal Expenses: ₦{total:,.2f}")
