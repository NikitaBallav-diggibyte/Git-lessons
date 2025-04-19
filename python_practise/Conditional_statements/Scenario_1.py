# 1. Access Control System
# A company is designing an access control system for employees.
# Each employee enters a 4-digit PIN. If they fail to enter the correct PIN in 3 attempts, access should be denied, and a report should be generated for security.
#
# Challenge:
# Write logic that handles this PIN verification system.
# Track the number of failed attempts, and output a different message for each type of result: success, failure, and blocked access.
#
# Hint: You’ll need a loop, a condition, and a counter.

def access_control(max_attempt, correct_pin):
    counter = 0

    for _ in range(0,3):
        pin=int(input("enter your pin: "))
        counter+=1
        if pin==correct_pin:
            print("Success")
            break
        else:
            if counter<max_attempt:
                print("failure: try again")
            else:
                print("access blocked.")


access_control(3, 2345)