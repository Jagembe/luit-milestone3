# Iterating lists

# List of top cities
top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Iterating over the list using a for loop to access each element
for city in top_cities:
    # Print the current city
    print("Current city:", city)

# List of top cities again, for demonstration of index-based iteration
top_cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"]

# Iterating over the range of indices from 0 to the length of the list
for city_index in range(len(top_cities)):
    # Print the current index and the city at that index
    print("Current index:", city_index, "| Current city:", top_cities[city_index])

# List of spending amounts
spendings = [32.24, 18.65, 23.45, 78.32, 5.23]

# Initialize the sum variable to keep track of the total spending
sum = 0.0

# Iterating over the list of spendings
for spending in spendings:
    # Add each spending amount to the sum
    sum += spending

# Print the total money spent
print("money spent:", sum)
