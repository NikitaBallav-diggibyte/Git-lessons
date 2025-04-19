#  2. E-commerce Discount Logic
# An e-commerce company is working on a new feature to offer discounts to customers based on their total cart value.
#
# Task:
# Design a script that:
#
# Accepts multiple item prices from a customer (use a loop)
#
# Adds them to calculate the total cart value
#
# Applies a discount based on these rules:
#
# ₹5000 → 20% discount
#
# ₹3000–₹4999 → 10% discount
#
# < ₹3000 → No discount
#
# Outputs the final amount payable.
#
# Hint: You’ll need a loop to collect prices and if-elif-else to apply discount.

import pandas as pd

def discount():
    no_of_items = int(input("Number of distinct items: "))
    print("enter item name quantity and unit price separated with space: ")
    data=[]
    for _ in range(no_of_items):
        item= input().split()
        name= item[0]
        quantity= int(item[1])
        unit_price=int(item[2])
        data.append([name,quantity,unit_price])

    table=pd.DataFrame(data, columns=["Item_name", "Quantity", "Unit_price"])
    table["Total_price"]=table["Quantity"]*table["Unit_price"]
    total_amt= sum(table["Total_price"])

    if total_amt>=5000:
        print("Congratulations..You received a discount of 20% on your total amount of Rs.", total_amt)
        discount_amt= 1-(20/100)
        total_amt= total_amt*discount_amt
        print("Payable amount: ", total_amt)
    elif 3000<=total_amt<=4999:
        print("Congratulations..You received a discount of 10% on your total amount of Rs.", total_amt)
        discount_amt = 1 - (10 / 100)
        total_amt = total_amt * discount_amt
        print("Payable amount: ", total_amt)
    else:
        print("Payable amount: ", total_amt)


discount()







