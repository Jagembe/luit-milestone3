# Create a list of top cities in the U.S.
top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Print the entire list of cities
print(top_cities)

# Accessing elements using positive and negative indexes
# Print the 4th city in the list (index 3, because indexing starts at 0)
print(top_cities[3])

# Print the 2nd city in the list using a negative index (index -4 refers to the 2nd item from the start)
print(top_cities[-4])

# Slicing the list to create and print sublists
# Print a sublist containing the 1st and 2nd cities (from index 0 to 1, as slicing is exclusive of the stop index)
print(top_cities[0:2])

# Print a sublist starting from the 4th city to the end of the list (from index 3 onward)
print(top_cities[3:])

# Print the entire list using slicing (from the beginning to the end of the list)
print(top_cities[:])

# Attempt to slice and print a sublist that is out of range (indexes 10 to 14)
# This will result in an empty list since these indexes do not exist in the list
print(top_cities[10:15])


