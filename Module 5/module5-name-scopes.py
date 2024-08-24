# --- First Part of the Script ---

# Define a function 'show_truth' that declares a local variable 'mysterious_var'.
def show_truth():
    # 'mysterious_var' is a local variable within this function, separate from any outside variables.
    mysterious_var = "New Surprise!"
    # Print the local 'mysterious_var'.
    print(mysterious_var)

# Here, 'mysterious_var' is a global variable, separate from the local variable in 'show_truth'.
mysterious_var = "Surprise!"
# Print the global 'mysterious_var'.
print(mysterious_var)  # Output: "Surprise!"

# Call the function 'show_truth'.
show_truth()  # Output: "New Surprise!" (this is the local variable inside the function)

# Print the global 'mysterious_var' again.
print(mysterious_var)  # Output: "Surprise!" (the global variable remains unchanged)


# --- Second Part of the Script ---

# Redefine the 'show_truth' function, this time expecting 'mysterious_var' to be a mutable object.
def show_truth():
    # Append "New Surprise!" to the global list 'mysterious_var'.
    mysterious_var.append("New Surprise!")
    # Print the modified 'mysterious_var'.
    print(mysterious_var)

# Now 'mysterious_var' is a global list.
mysterious_var = ["Surprise!"]
# Print the global 'mysterious_var' before calling the function.
print(mysterious_var)  # Output: ["Surprise!"]

# Call the function 'show_truth' which modifies the global list.
show_truth()  # Output: ["Surprise!", "New Surprise!"]

# Print the global 'mysterious_var' again to show that it has been modified by the function.
print(mysterious_var)  # Output: ["Surprise!", "New Surprise!"]
