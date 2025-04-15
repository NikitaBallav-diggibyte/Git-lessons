brand= int(input("Enter branding expenses: "))
travel= int(input("Enter travel expenses: "))
food= int(input("Enter food expenses: "))
logistics= int(input("Enter logistics expenses: "))
total_expense=brand+travel+food+logistics

print("Total_expense= ", brand+travel+food+logistics)
print("Branding_expenses_percentage = ", (brand / total_expense) * 100, "%")
print("Travel_expenses_percentage= ", (travel/total_expense)*100,"%")
print("Food_expenses_percentage= ", (food/total_expense)*100,"%")
print("Logistics_expenses_percentage= ", (logistics/total_expense)*100,"%")

