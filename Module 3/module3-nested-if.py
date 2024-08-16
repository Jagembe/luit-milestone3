# Nested if statments = an if statemnts inside of another if statement
# Prompt the user to answer if they like traveling with 'y' or 'n'
answer_a = input("Do you like traveling? y/n: ")

# Check if the user answered 'y' (yes) to liking traveling
if answer_a == "y":
    # If they like traveling, ask if they like Asia with 'y' or 'n'
    answer_b = input("And do you like Asia? y/n: ")
    
    # Check if the user answered 'y' (yes) to liking Asia
    if answer_b == "y":
        # If they like Asia, print that they can win a ticket to Thailand
        print("Excellent! You can win a ticket to Thailand!")
    else:
        # If they don't like Asia, print a message expressing disappointment
        print("Sorry to hear that!")
else:
    # If the user doesn't like traveling, print a message expressing disappointment
    print("Sorry to hear that!")
