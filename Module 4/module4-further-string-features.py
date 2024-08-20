# Define a string variable 'fav_band' with the value "Tame Impala"
fav_band = "Tame Impala"

# Print the character at index 6 in the string 'fav_band'
# Python uses zero-based indexing, so index 6 corresponds to the 7th character
# In "Tame Impala", index 6 is the character "I"
print(fav_band[6])  # Output: I

# ---------------------------------------------------------------

# Define the string variable 'fav_band' again
fav_band = "Tame Impala"

# Print the substring from the beginning of 'fav_band' up to (but not including) index 6
# This will output the first 6 characters of the string "Tame I"
print(fav_band[:6])  # Output: Tame I

# ---------------------------------------------------------------

# Define a string variable 'text' with the value "please capitalize me"
text = "please capitalize me"

# Convert the entire string 'text' to uppercase letters
# The upper() method returns a new string where all characters are capitalized
text_cap = text.upper()

# Print the capitalized version of the string
print(text_cap)  # Output: PLEASE CAPITALIZE ME

# ---------------------------------------------------------------

# Prompt the user to input a number and store the input as a string in 'user_number'
user_number = input("Please provide a number: ")

# Check if the input string 'user_number' contains only numeric characters
# The isnumeric() method returns True if all characters in the string are digits, otherwise False
if user_number.isnumeric():
    # If 'user_number' is a valid number, print a confirmation message
    print("Thank you, that's a correct number!")
else:
    # If 'user_number' is not a valid number, print an error message along with the invalid input
    print("Sorry", user_number, "is not a number!")


