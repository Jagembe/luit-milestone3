# String variables
# Assign the string "John Snow" to the variable 'name_original'
name_original = "John Snow"

# Assign the value of 'name_original' to 'name_new'. 
# At this point, both variables reference the same string "John Snow"
name_new = name_original

# Change the value of 'name_original' to "Samuel Jackson"
# This does not affect 'name_new' because strings are immutable, 
# and 'name_new' still references the original string "John Snow"
name_original = "Samuel Jackson"

# Print the current values of 'name_original' and 'name_new'
print(name_original, name_new)
# Output: Samuel Jackson John Snow

# ---------------------------------------------------------------

# List variables
# Assign a list [1, 2, 3] to the variable 'list_original'
list_original = [1, 2, 3]

# Assign the reference of 'list_original' to 'list_new'.
# Both variables now reference the same list object in memory
list_new = list_original

# Modify the first element of the list 'list_original' to -5
# This change will be reflected in both 'list_original' and 'list_new' 
# because they reference the same list object
list_original[0] = -5

# Print the current values of 'list_original' and 'list_new'
print("Original", list_original, "\nNew:", list_new)
# Output: Original [-5, 2, 3] 
#         New: [-5, 2, 3]
# UH OH! looks like we're getting the same result after modifying. Solution: use slicing [:]

# ---------------------------------------------------------------

# Reassign the list [1, 2, 3] to 'list_original' 
list_original = [1, 2, 3]

# Create a new list 'list_new' by copying all elements of 'list_original' 
# using slicing. Now 'list_new' references a different list object in memory.
list_new = list_original[:]

# Modify the first element of the list 'list_original' to -5
# This change will NOT affect 'list_new' because they reference different lists
list_original[0] = -5

# Print the current values of 'list_original' and 'list_new'
print("Original", list_original, "\nNew:", list_new)
# Output: Original [-5, 2, 3] 
#         New: [1, 2, 3]

# ---------------------------------------------------------------

# Reassign the list [1, 2, 3] to 'list_original'
list_original = [1, 2, 3]

# Create a new list 'list_new' by copying the first two elements of 'list_original'
# Now 'list_new' is a shorter list and references a different list object
list_new = list_original[:2]

# Modify the first element of the list 'list_original' to -5
# This change will NOT affect 'list_new' because they reference different lists
list_original[0] = -5

# Print the current values of 'list_original' and 'list_new'
print("Original", list_original, "\nNew:", list_new)
# Output: Original [-5, 2, 3] 
#         New: [1, 2]

# ---------------------------------------------------------------

# Reassign the list [1, 2, 3] to 'list_original'
list_original = [1, 2, 3]

# Create a new list 'list_new' by copying all elements of 'list_original'
# using slicing. This creates a new list object in memory.
list_new = list_original[:]

# Print the value of 'list_new'
print(list_new)
# Output: [1, 2, 3]
