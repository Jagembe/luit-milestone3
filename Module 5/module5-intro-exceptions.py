# Exceptions

try:
    # Prompt the user to enter an integer value.
    # The input function returns a string, so we use int() to convert it to an integer.
    value = int(input("Enter an integer: "))
    
    # Attempt to calculate the inverse of the value.
    # This will raise a ZeroDivisionError if the user inputs 0.
    print("The inverse of", value, "is", 1/value)
    
# Handle the case where the input cannot be converted to an integer (e.g., if the user inputs "a").
except ValueError:
    print("You did not provide a number, so I will not calculate the inverse")

# Handle the case where the user inputs 0, which would cause a division by zero.
except ZeroDivisionError:
    print("You provided a 0 and division by 0 is not possible, sorry")

# Catch any other exceptions that are not explicitly handled above.
except Exception as e:
    # Print a generic error message.
    print("Something strange happened here, sorry")

    # Optionally, print the actual error message for debugging purposes.
    # This is useful for identifying unexpected issues.
    print("Error details:", str(e))
