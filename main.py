print("Welcome to Student Budget Tracker!")

income = float(input("Enter your monthly income $"))
expenses = []
while True:
  expense = input("Enter an expense amount or type 'done' to finish: $")
  if expense.lower() == "done":
    break
  expenses.append(float(expense))
    
total_expenses = sum(expenses)
remaining = income - total_expenses 

print("n--- monthly budget summary ---")
print("Monthly income: $", round(income, 2))
print("Total expenses: $", round(total_expenses, 2))
print("Remaining balance: $", round(remaining, 2))
