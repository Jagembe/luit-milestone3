# Checking list presence
# Iterate over each character in the string "happy message"
for char in "happy message":
    # Print the current character
    print(char)

# ---------------------------------------------------------------

# List of invited guests
invited_guest = ["Kate", "Adam", "Kerry", "Joe", "Anne", "Marie"]

# Prompt the user to enter their name and store it in the variable 'name'
name = input("What is your name? ")

# Check if the entered name is in the list of invited guests
if name in invited_guest:
    # If the name is found in the list, print a welcome message
    print("Welcome!")
else:
    # If the name is not found in the list, print a message indicating the user is not invited
    print("You are not invited!")

# ---------------------------------------------------------------

# List of invited guests again
invited_guest = ["Kate", "Adam", "Kerry", "Joe", "Anne", "Marie"]

# Prompt the user to enter their name and store it in the variable 'name'
name = input("What is your name? ")

# Check if the entered name is NOT in the list of invited guests
if name not in invited_guest:
    # If the name is not in the list, print a message indicating the user is not invited
    print("You are not invited")
else:
    # If the name is in the list, print a welcome message
    print("Welcome!")

