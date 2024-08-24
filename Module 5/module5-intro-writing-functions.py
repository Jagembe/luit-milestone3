# Creating functions
# Define a function named 'greet' that takes no parameters.
def greet():
    """
    This function prints a greeting message.
    
    The function is simple and doesn't take any arguments.
    It demonstrates the basic structure of a function in Python.
    """
    # Print a greeting message to the console.
    print("Hello, my dear!")

# Call the 'greet' function to execute its code.
greet()

# --- Enhancements and Additional Examples ---

# 1. Function with Parameters
def greet_person(name):
    """
    Greets a person by name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    This demonstrates how to pass arguments to a function.
    """
    print(f"Hello, {name}!")

# Call the function with an argument
greet_person("Alice")

# 2. Function with a Return Value
def get_greeting(name):
    """
    Returns a greeting message for a person by name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: A greeting message.
    
    This demonstrates how to return a value from a function.
    """
    return f"Hello, {name}!"

# Store the returned greeting in a variable and print it
greeting_message = get_greeting("Bob")
print(greeting_message)

# 3. Function with a Default Parameter
def greet_with_default(name="stranger"):
    """
    Greets a person by name, with a default name if none is provided.
    
    Parameters:
    name (str, optional): The name of the person to greet. Defaults to "stranger".
    
    This demonstrates how to use default parameter values.
    """
    print(f"Hello, {name}!")

# Call the function without an argument to use the default
greet_with_default()

# Call the function with an argument to override the default
greet_with_default("Charlie")

# 4. Docstrings and Fu
