# available logical operators
# < less than
# > greather than
# <= less than or equal
# >= greather than or equal
# == equals
# != not equals

# Prompt the user to input a password
password = input("Do you know the secret password? ")

# Check if the input password is not equal to "--secret"
if password != "--secret":
    # If the password is incorrect, print "not correct"
    print("not correct")
else:
    # If the password is correct, print "correct password"
    print("correct password")

# Check if 2 is equal to 2 (this is always true)
if 2 == 2:
    # Print "true" since the condition is true
    print("true")

# Check if 2 is equal to 1 (this is always false)
if 2 == 1:
    # This will not execute because the condition is false
    print("true")

# Check if 2 is equal to 2.0 (this is true because Python considers them equal)
if 2 == 2.0:
    # Print "true" since the condition is true
    print("true")
