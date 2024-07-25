import pandas as pd
import matplotlib.pyplot as plt
class PersonalFinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])

    def add_transaction(self, date, category, amount, trans_type):
        new_transaction = pd.DataFrame([[date, category, amount, trans_type]], 
                                       columns=["Date", "Category", "Amount", "Type"])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

    def view_summary(self):
        print("Summary:")
        print(self.transactions.groupby(["Type", "Category"]).sum())

    def plot_expenses(self):
        expense_data = self.transactions[self.transactions["Type"] == "Expense"]
        expense_summary = expense_data.groupby("Category").sum()
        expense_summary.plot(kind="pie", y="Amount", autopct='%1.1f%%')
        plt.title("Expenses Breakdown")
        plt.show()

    def plot_income(self):
        income_data = self.transactions[self.transactions["Type"] == "Income"]
        income_summary = income_data.groupby("Category").sum()
        income_summary.plot(kind="pie", y="Amount", autopct='%1.1f%%')
        plt.title("Income Breakdown")
        plt.show()
def main():
    tracker = PersonalFinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Plot Expenses")
        print("4. Plot Income")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            trans_type = input("Enter type (Expense/Income): ")
            tracker.add_transaction(date, category, amount, trans_type)
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            tracker.plot_expenses()
        elif choice == '4':
            tracker.plot_income()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
