# Get rid of duplicates
def unique(input_list=[]):
    # Initialize an empty list to store the unique elements
    to_return = []
    
    # Loop through each element 'el' in the provided 'input_list'
    for el in input_list:
        # Check if the current element 'el' is not already in 'to_return'
        if el not in to_return:
            # If 'el' is unique (not in 'to_return'), add it to 'to_return'
            to_return.append(el)
    
    # After processing all elements, return the list 'to_return' which now contains only unique elements
    return to_return

# Call the 'unique' function with a list containing duplicates
# This will print: [1, 2, 3, 4, 5], since all duplicates are removed
print(unique([1, 2, 2, 3, 4, 4, 4, 5]))

# --------------------------------------

def unique(input_list=None):
    # Check if 'input_list' is None, if so, assign an empty list to it
    if input_list is None:
        input_list = []
    to_return = []
    for el in input_list:
        if el not in to_return:
            to_return.append(el)
    return to_return

# --------------------------------------

def unique(input_list=None):
    if input_list is None:
        input_list = []
    seen = set()  # To track elements that have already been added
    to_return = []
    for el in input_list:
        if el not in seen:  # O(1) check
            seen.add(el)    # O(1) insertion
            to_return.append(el)  # Maintain order in 'to_return'
    return to_return

print(unique([1, 2, 2, 3, 4, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique([10, 20, 20, 30]))          # Output: [10, 20, 30]
print(unique([1, 2, 3]))                 # Output: [1, 2, 3] - Already unique
print(unique([]))                        # Output: [] - Empty list


