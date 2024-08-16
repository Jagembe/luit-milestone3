# Refund Policy Helper

# Prompt the user to input how many days ago they purchased the item and convert the input to an integer
purchased_days_ago = int(input("How many days ago have you purchased the item? "))

# Prompt the user to answer if they have used the item with 'y' or 'n'
is_used = input("Have you used the item at all [y/n]? ")

# Prompt the user to answer if the item has broken down on its own with 'y' or 'n'
is_broken = input("Has the item broken down on its own [y/n]? ")

# Check if the item was purchased less than 10 days ago and has not been used, 
# or if the item has broken down on its own
if purchased_days_ago < 10 and is_used == "n" or is_broken == "y":
    # If either condition is true, print that the user can get a refund
    print("You can get a refund.")
else:
    # If neither condition is true, print that the user cannot get a refund
    print("You cannot get a refund.")


