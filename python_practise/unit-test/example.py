# Red Step: write the test and run it (it should fail)

# "Joe" --> "Welcome Joe"

# Green step: write the logic so that the test succeeds

# Refactor step: Improve the code

def greet_person(name):
    ## Case when there is nothing mentioned inside the function and all the test fails
    #pass
    ## case when the test succeeds
    capitalized_name= name.capitalize()
    greeting_message= f'Welcome {capitalized_name}'
    return greeting_message
    ## case when the test fails when the name is not capitalized
    # return f"Welcome {name}"

def can_drink_alcohol(age):
    ## case when there is nothing mentioned inside the function and all the test fails
    # pass

    ## Case when the test succeeds
    return age>=18