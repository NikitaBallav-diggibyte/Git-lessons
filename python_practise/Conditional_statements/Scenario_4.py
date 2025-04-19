# 4. Spending Pattern Detector
# You’re working for a fintech startup that needs to analyze a user’s weekly expenses over a month (4 weeks).
# The goal is to alert the user if they overspend (over ₹4000) in any week, or stay under budget for all.
#
# Task:
#
# Collect 4 weekly expense inputs.
#
# Print “Overspending detected in Week X” if any week crosses ₹4000.
#
# At the end, tell them how many weeks they overspent, and how much in total they spent.
#
# This one tests your control flow, loop logic, and variables.

def analyze_expenses():
    expense_list = []

    for i in range(1, 5):
        print("Enter your total expense for Week", i)
        user_expense = int(input())
        expense_list.append(user_expense)

    no_of_week = 0

    for idx, amount in enumerate(expense_list, start=1):  # start=1 to match "Week 1"
        if amount > 4000:
            no_of_week += 1
            print(f"Overspending detected in Week {idx} (₹{amount})")

    print("\nSummary Report:")
    print("Total number of overspending weeks:", no_of_week)
    print("Total expense for the month: ₹", sum(expense_list))

# Call the function
analyze_expenses()

