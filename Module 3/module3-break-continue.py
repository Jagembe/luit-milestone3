# break instructions stop the loop and moves on to the next instruction
# Infinite loop to repeatedly ask for user input
while True:
    # Prompt the user to enter their name or "EXIT" to stop the program
    name = input("Enter your name or EXIT to close the program: ")
    
    # Check if the user entered "EXIT"
    if name == "EXIT":
        break  # Exit the loop if the user wants to close the program
    
    # Greet the user by printing their name
    print("Hello", name)

# Loop through numbers 1 to 20
for i in range(1, 21):
    # Check if the current number is divisible by 5
    if i % 5 == 0:
        continue  # Skip the current iteration if the number is divisible by 5
    
    # Print the number if it's not divisible by 5
    print(i)
