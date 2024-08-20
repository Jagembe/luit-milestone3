# Python guessing game
# Start an infinite loop
while True:
    # Prompt the user to input their answer for the year Python 1.0 was released
    # The input is converted to an integer and stored in the variable 'answer'
    answer = int(input("When was Python 1.0 released? "))
    if answer > 1994: # Check if the user's answer is greater than 1994
        print("It was earlier than that!") # If the answer is too late, inform the user that the release year was earlier
    elif answer < 1994:  # Check if the user's answer is less than 1994
        print("It was later than that!") # If the answer is too early, inform the user that the release year was later
    else: # If the answer is exactly 1994 (the correct year)
        print("Correct!") # Congratulate the user for the correct answer
        break # Break out of the loop since the correct answer was provided

