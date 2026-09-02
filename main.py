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
