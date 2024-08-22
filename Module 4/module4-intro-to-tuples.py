# Ways to write tuples. The round brackets are optional but you must include a comma in the tuple.
empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3 # If there are multiple values, you dont have to put a comma after the last value but you can.
print(three_el_tuple)

# ----------------------------------------------------

# Mutability (revisable code)
user_data = ("John", "American", 1964)
user_data = ("Katya", "Russian", 1980)
# Tuples are immutable meaning you can add or remove anything from the data above ex: .append
user_data.append("teacher") # this will give you an attribute error
del user_data[0] # this will also give you an error. it doesn't support item deletion
# you can print a single element of a tuple but you cannot change, add, or delete an element in a tuple
# strings are also immutable when it comes to changing a single char in the string
message = "Welcome"
message[0] = "w" # this will not work for string and will throw an error