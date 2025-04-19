# 3. Subsidy Eligibility Checker
# A government scheme gives travel subsidies to people based on their age:
#
# Below 5 or above 60 → Free travel
#
# Age 5 to 18 → 50% subsidy
#
# Age 19 to 60 → No subsidy
#
# Real Challenge:
# Write a program that asks for a list of people’s ages and prints the eligible subsidy type for each of them.
#
# Hint: Try using a loop with conditional checks.
def subsidy():

    no_of_people= int(input("How many members are there? "))
    list_of_age= []
    for i in range(1, no_of_people+1):
        print("enter age of member ",i)
        age= int(input())
        list_of_age.append(age)

    for j in list_of_age:
        if j<5 or j>60:
            print("Free travel for", j)
        elif 5<=j<=18:
            print(j, "Congrats You received 50% subsidy")
        else:
            print("Sorry, no subsidy for", j)


subsidy()
