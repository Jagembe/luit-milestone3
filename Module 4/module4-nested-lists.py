# Nested lists 

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Define a list of country names
countries = ["UK", "US", "Germany"]

# Redefine the 'countries' list to include both integers and strings
# It is generally advisable to avoid mixing data types within a list 
# unless there's a specific reason, as it can make the list harder to manage
countries = [1, "UK", 2, "US"]  # Avoid mixing data types in a list unless necessary

# ---------------------------------------------------------------

# Lists can have other lists as elements, making them 2D (or nested) lists
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]

# Access the first list within 'cells', which contains ["A1", "A2", "A3"]
print(cells[0])  # Output: ['A1', 'A2', 'A3']

# ---------------------------------------------------------------

# Access the first element of the first list within 'cells'
print(cells[0][0])  # Output: A1

# ---------------------------------------------------------------

# Access the second element of the first list within 'cells'
print(cells[0][1])  # Output: A2

# ---------------------------------------------------------------

# Access the third element of the second list within 'cells'
print(cells[1][2])  # Output: B3

# ---------------------------------------------------------------

# Iterating over each list (or row) within 'cells'
cells = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for x in cells:
    # Print the entire row (each sublist) in 'cells'
    print("Elements:", x)
# Output: 
# Elements: ['A1', 'A2', 'A3']
# Elements: ['B1', 'B2', 'B3']

# ---------------------------------------------------------------

# Nested for loops to iterate over each element in each row of 'cells'
for x in cells:
    # Iterate over each element in the current row 'x'
    for y in x:
        # Print each individual element
        print("Elements:", y)
# Output:
# Elements: A1
# Elements: A2
# Elements: A3
# Elements: B1
# Elements: B2
# Elements: B3

# ---------------------------------------------------------------

# Another example of iterating over a 2D list 'table', 
# where each row is printed element by element
table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        # Print each cell in the row
        print("Elements:", cell)
# Output:
# Elements: A1
# Elements: A2
# Elements: A3
# Elements: B1
# Elements: B2
# Elements: B3

# ---------------------------------------------------------------

# This code prints the 'table' in a way that resembles an Excel table,
# with each cell in a row printed on the same line
table = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
for row in table:
    for cell in row:
        # Print each cell followed by a space, without a newline
        print(cell, "", end="")
    # Print a newline after each row
    print()
# Output:
# A1 A2 A3 
# B1 B2 B3 

# ---------------------------------------------------------------

# Creating a 4x5 table (2D list) using list comprehension
# The table consists of 4 rows, each containing the numbers 1 through 5
table = [[i for i in range(1, 6)] for j in range(4)]

# Print the entire table
print(table)
# Output:
# [[1, 2, 3, 4, 5], 
#  [1, 2, 3, 4, 5], 
#  [1, 2, 3, 4, 5], 
#  [1, 2, 3, 4, 5]]
