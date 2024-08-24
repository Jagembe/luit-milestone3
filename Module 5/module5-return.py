def get_average(input_numbers):
    # Initialize a variable 'sum' to store the cumulative total of the numbers
    sum = 0.0

    # Iterate through each number in the input list 'input_numbers'
    for number in input_numbers:
        # Add each number to 'sum'
        sum += number

    # Calculate the average by dividing the sum by the number of elements in the list
    # len(input_numbers) returns the count of numbers in the list
    average = sum / len(input_numbers)
    
    # Return the calculated average
    return average

# Calling the 'get_average' function with a list of floats and printing the result
print("The average is:", get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

# Store the average of the list in a variable
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])

# Conditional check: if the average is greater than 5.0, print a message
if average > 5.0:
    print("The average is too high!")

def get_average(input_numbers):
    # Initialize a variable 'sum' to store the cumulative total of the numbers
    sum = 0.0

    # Iterate through each number in the input list 'input_numbers'
    for number in input_numbers:
        # Add each number to 'sum'
        sum += number

    # Calculate the average by dividing the sum by the number of elements in the list
    average = sum / len(input_numbers)
    
    # Return the calculated average
    return average

    # This print statement is unreachable due to the return statement above
    # It will never be executed. Consider removing or repositioning it.
    print("Show me!")

# This function call passes a single-element list [2] to 'get_average'
# Since there's only one number, the average will be that number itself
get_average([2])

def is_first_lats_equal(number_list):
    # Check if the list is empty; if so, return None (implicitly)
    if len(number_list) == 0:
        return
    
    # Compare the first and last elements of the list
    if (number_list[0] == number_list[-1]):
        # If they are equal, return True
        return True
    else:
        # Otherwise, return False
        return False

# The following calls test the 'is_first_lats_equal' function:
print(is_first_lats_equal([10, 20, 30, 40, 10]))  # True, since 10 == 10
print(is_first_lats_equal([10, 20, 30, 40, 50]))  # False, since 10 != 50
print(is_first_lats_equal([]))  # None, as the list is empty


