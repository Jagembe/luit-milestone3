# Changing element positions in lists
# Prompt the user to enter the first number and store it as a string in the variable 'first'
first = input("Enter first number: ")

# Prompt the user to enter the second number and store it as a string in the variable 'second'
second = input("Enter second number: ")

# Print the values of 'first' and 'second' before swapping
print("Before swapping:", first, second)

# Swap the values of 'first' and 'second' in a single line using tuple unpacking
first, second = second, first

# Print the values of 'first' and 'second' after swapping
print("After swapping:", first, second)

# ---------------------------------------------------------------

# List of top cities
top_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Swap the first element (index 0) with the last element (index 4) in the list
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]

# Print the list after swapping the elements
print(top_cities)

# ---------------------------------------------------------------

# Reset the list of top cities
top_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Sort the list of cities in alphabetical order
top_cities.sort()

# Print the sorted list of cities
print(top_cities)

# ---------------------------------------------------------------

# List of random numbers
random_numbers = [2, 7, 3, 1, -8, 4]

# Sort the list of numbers in ascending order (from lowest to highest)
random_numbers.sort()

# Print the sorted list of numbers
print(random_numbers)

# ---------------------------------------------------------------

# Another list of random numbers
random_numbers = [3, 2, 6, 9, -3, 0]

# Sort the list of numbers in descending order (from highest to lowest) using the 'reverse=True' parameter
random_numbers.sort(reverse=True)

# Print the list after sorting in descending order
print(random_numbers)

# ---------------------------------------------------------------

# Reset the list of top cities
top_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Print a new sorted list of cities using the 'sorted' function without modifying the original list
print(sorted(top_cities))

# Print the original list to show it remains unchanged
print(top_cities)
