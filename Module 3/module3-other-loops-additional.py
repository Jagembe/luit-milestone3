# The pass instruction makes the code do nothing. If you remove pass the code will not run and will throw an error.
# Loop over a range of numbers from 0 to 10 (inclusive)
for i in range(11):
    pass  # 'pass' is a placeholder that does nothing; this loop effectively does nothing

# Nested loop to create a multiplication table
for a in range(1, 6):  # Outer loop: iterates over numbers 1 to 5 (inclusive)
    for b in range(1, 6):  # Inner loop: iterates over numbers 1 to 5 (inclusive)
        # Print the multiplication of 'a' and 'b' in a formatted string
        print(a, "x", b, "=", a * b)

# Initialize variable 'i' with a value of 2
i = 2
# Start a while loop that continues as long as 'i' is less than 5
while i < 5:
    print(i)  # Print the current value of 'i'
    i += 1  # Increment 'i' by 1 in each iteration

# The 'else' block is executed after the while loop completes (i.e., when i >= 5)
else:
    print("else:", i)  # Print the final value of 'i' after the loop terminates
