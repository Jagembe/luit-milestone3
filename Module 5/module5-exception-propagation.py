# Function to get the day of the user's birthday
def get_day(user_info):
    # Prompt the user to enter the day of their birthday as an integer
    day = int(input("What is the day of your bday? "))
    
    # Append the day to the user_info list
    user_info.append(day)

# Function to get the month of the user's birthday
def get_month(user_info):
    # Prompt the user to enter the month of their birthday as an integer
    # This should be a number between 1 and 12
    month = int(input("What is the month (1-12) of your bday? "))
    
    # Append the month to the user_info list
    user_info.append(month)

# Function to get the year of the user's birthday
def get_year(user_info):
    # Prompt the user to enter the year of their birthday as an integer
    year = int(input("What is the year of your bday? "))
    
    # Append the year to the user_info list
    user_info.append(year)

# Function to collect the user's birthday information
def get_user_bday(user_info):
    try:
        # Attempt to get the day, month, and year of the user's birthday
        # If an error occurs in any of these functions, the exception will be caught here
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        
        # If all inputs are valid, print the collected birthday information
        print("So your bd is", user_info)
    
    # Handle the case where the user inputs non-integer values
    except ValueError:
        # Print an error message if the user enters incorrect data
        print("You entered incorrect data, bye!")

# Main script execution
print("Hi, I will collect some info about your bday!")

# Initialize an empty list to store the user's birthday information
user_info = []

# Call the function to get the user's birthday
get_user_bday(user_info)

