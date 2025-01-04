# Expense Tracker Program

# List to store expenses
expenses = []

def add_expense():
    """Function to add an expense"""
    name = input("Enter the name of the expense: ")
    try:
        amount = float(input("Enter the amount: "))
        expenses.append({"name": name, "amount": amount})
        print(f"'{name}' has been added as an expense of {amount}.\n")
    except ValueError:
        print("Invalid input! Amount must be a number.\n")

def view_expenses():
    """Function to view all expenses"""
    if not expenses:
        print("No expenses have been added yet.\n")
        return

    print("\nYour Expense List:")
    total = 0
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']} units")
        total += expense['amount']
    print(f"Total Expense: {total} units\n")

def main():
    """Menu-driven program"""
    while True:
        print("== Expense Tracker Menu ==")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
