# Joining multiple conditions using Boolean Oprerators. There are 3 boolean operators:
# and
# or
# not

# Prompt the user to input their age and convert it to an integer
user_age = int(input("What is your age? "))

# Prompt the user to input their country
user_country = input("What is your country? ")

# Check if the user's age is less than 25 and if their country is Germany
if user_age < 25 and user_country == "Germany":
    # If both conditions are true, print that they can apply for the German student exchange programme
    print("You can apply for a German student exchange programme")
else:
    # If either condition is false, print that they do not qualify
    print("Sorry, you do not qualify")

# Prompt the user to input their country again
user_country = input("Where do you come from? ")

# Check if the user's country is Sweden, Denmark, or Norway
if user_country == "Sweden" or user_country == "Denmark" or user_country == "Norway":
    # If the country matches any of these, print that they can apply for the Scandinavian student exchange programme
    print("You can apply for a Scandinavian student exchange programme")
else:
    # If the country doesn't match, print that they do not qualify
    print("Sorry, you do not qualify")

# Prompt the user to input their country once more
user_country = input("Where do you come from? ")

# Check if the user's country is not Germany
if not user_country == "Germany":
    # If the user is not from Germany, print that they are not from Germany
    print("you are not from Germany")
else:
    # If the user is from Germany, print that they are from Germany
    print("you are from Germany")

# Prompt the user to input their age and country again
user_age = int(input("What is your age? "))
user_country = input("What is your country? ")

# Check if the user is not from Germany and younger than 25, or if they are from Germany and younger than 23
if not user_country == "Germany" and user_age < 25 or user_country == "Germany" and user_age < 23:
    # If any of these conditions are true, print that they qualify
    print("You qualify!")
else:
    # If none of the conditions are met, print that they don't qualify
    print("You don't qualify!")


# Boolean priority order
# 1. not
# 2. and
# 3. or   
# you can use brackets in a complex script to help you understande what is being executed and the order of execution 