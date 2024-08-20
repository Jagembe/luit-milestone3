# Create a list of cities including some in the U.S. and one international city
top_cities = ["New York City", "Los Angeles", "Singapore", "Chicago", "Houston", "Phoenix"]

# Delete the city at index 2 (which is "Singapore") from the list
del top_cities[2]
# Print the modified list after deletion
# The list now contains: ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(top_cities)

# Delete all cities from index 3 onwards (removes "Houston" and "Phoenix")
del top_cities[3:]
# Print the modified list after slicing deletion
# The list now contains: ["New York City", "Los Angeles", "Chicago"]
print(top_cities)

# Delete all the elements in the list (clear the list)
del top_cities[:]
# Print the modified list after clearing
# The list is now empty: []
print(top_cities)

# Delete the list object itself from memory
del top_cities

# Attempt to print the list after deleting it
# This will throw a NameError because 'top_cities' no longer exists
print(top_cities)
