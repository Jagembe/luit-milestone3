# while loops

# Initialize the counter variable
counter = 1

# Start a loop that runs as long as the counter is less than 11
while counter < 11:
    print(counter)  # Print the current value of the counter
    counter += 1    # Increment the counter by 1

# Print a message when the loop finishes
print("Finished!")

secret_number = 14

# Print the title and instructions for the Secret Number Game
print("""
==========================
=== SECRET NUMBER GAME ===
==========================
""")


user_input = int(input("Try to guess the secret number from 0 to 20: "))

# Start a loop that continues until the user guesses the correct number
while user_input != secret_number:
    print("Wrong!")  # Inform the user that their guess was incorrect
    # Prompt the user to guess again
    user_input = int(input("Try to guess the secret number from 0 to 20: "))

# Print a congratulatory message when the user guesses the secret number
print("Perfect! You have guessed the secret number.")
