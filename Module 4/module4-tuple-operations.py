# tuple operations
user_data = ("John", "American", 1964)
print(len(user_data))

user_data = ("John", "American", 1964)
if "American" in user_data:
    print("This person comes from the US!")

user_data = ("John", "American", 1964)
for element in user_data:
    print(element)

# This one is basically creating a new tuple since we know we cant modify elelments in a tuple
user_data = ("John", "American", 1964) + ("teacher", "male")
print(user_data)

numbers = (0, 1) * 10
print(numbers)

# How do we know when we should use tuples vs. lists?
# Lists usualy contain multiple elements of the same data type
male_name = ["Adam", "John", "Mark"] # all strings
us_temps = [97, 88, 67] # all int's
# A tuple would contain multiple elements that may not be the same data type 
user_data = ("John", "American", 1964) # mix of strings and int's. this would make more sense to use a tuple when mixing types

# This is a tuple as well
first = 5
second = 7
first, second = second, first