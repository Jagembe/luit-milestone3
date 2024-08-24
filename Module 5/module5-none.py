# --- Exploring the return value of the print() function ---

# The print() function outputs text to the console but doesn't return a value.
# Here, we're calling print() and storing its return value in 'print_return'.
print_return = print("Hello world")  # This prints "Hello world" to the console.

# Since print() returns None, 'print_return' will be None.
print(print_return)  # Output: None (because print() returns None)


# --- Understanding conditional statements and the None type ---

# Variable 'x' is explicitly set to None, a special value in Python that represents "nothing" or "no value".
x = None

# The first condition checks if 'x' is truthy (not None, not 0, not an empty sequence, etc.).
if x:
    print("None is True")
# The elif condition checks if 'x' is explicitly equal to False.
elif x is False:
    print("None is False")
# The else block runs if neither of the above conditions is met.
else:
    print("None is not True, or False, None is just None")
    # Output: "None is not True, or False, None is just None"

# --- Comparing 'is' vs '==' when checking for None ---

x = None

# 'is' checks for identity, meaning it checks if both sides refer to the same object in memory.
if x is None:
    print("yes")  # Output: "yes"

# '==' checks for equality, meaning it checks if the values are equivalent.
if x == None:
    print("it does")  # Output: "it does"

# It's best practice to use 'is None' when checking if a variable is None, rather than '== None'.


# --- Understanding the return value of functions ---

# Define a simple function that prints a greeting.
def greet():
    print("hello!")  # This function prints "hello!" to the console but does not explicitly return a value.

# Call the greet() function and store the return value in 'x'.
x = greet()  # This prints "hello!" but does not return anything, so 'x' will be None.

# Print the value of 'x'.
print(x)  # Output: None (because greet() does not return anything)
