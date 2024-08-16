# Prompt the user to input their age and convert it to an integer
user_age = int(input("What is your age? "))

# Check if the user's age is greater than 30
if user_age > 30:
    # If true, print that the user is over 30 years old
    print("You are over 30 years old")
    # Inform the user that they do not qualify
    print("Sorry, you do not qualify")

# Check if the user's age is exactly 30
elif user_age == 30:
    # If true, print that the user is exactly 30 years old
    print("You are exactly 30 years old")
    # Inform the user that they will need to meet additional conditions to qualify
    print("You will need to meet additional conditions to qualify")

# If the user's age is less than 30
else:
    # Print that the user is 30 years old or younger
    print("You are 30 years old or younger")
    # Inform the user that they qualify
    print("Congratulations, you qualify!")
