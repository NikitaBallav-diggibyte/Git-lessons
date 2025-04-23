try:
    a = int(input("Enter a number: "))
    print("10 /", a, "=", 10 / a)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("That's not a number!")
else:
    print("All good! 😄")
finally:
    print("This block always runs.")



try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print("Caught an error:", e)


a=int(input("enter a value for a: "))
b=int(input("enter a value for b: "))
l=[1,2,5,3,4,6]

# code will not terminate, instead will show the exception message
try:
    c=a/b
    print(c)
    print(l[10])
except:
    print("there is an error.")

# Printing the error
try:
    c=a/b
    print(c)
    print(l[10])
except Exception as e:
    print(e)

# handling exception with default value
try:
    c=a/b
    print(c)
    print(l[10])
except:
    print("there is an error: Using default value for b as 1.")
    b=1
    c=a/b
    print(c)


try:
    c=a/b
    print(c)
    print(l[10])
except IndexError as e:
    print("there is a index error: ")
except ZeroDivisionError as e:
    print("Denominator can't be zero: plz enter valid integer value")


try:
    c=a/b
    print(c)
    print(l[10])
except (ValueError,ZeroDivisionError)  as e:
    print("Error raised.")



# Raising an error

def register_user(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old to register.")
    else:
        print("✅ Registration successful!")

# Main program
try:
    user_age = int(input("Enter your age: "))
    register_user(user_age)
except ValueError as e:
    print("❌ Error:", e)
