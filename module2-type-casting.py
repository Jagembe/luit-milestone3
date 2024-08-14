# Type casting
# If you were to run this below program and enter you height right now you would get an error 
# you can't divide a string and a float
# height_cm = input("Height converter: enter your height in cm: ")
# print("Your height in feet is:", float_height_cm / 30.48 )

# Solution: Convert the "str" number into a "float" number
# Use the float() function
height_cm = input("Height converter: enter your height in cm: ")
float_height_cm = float(height_cm)
print("Your height in feet is:", float_height_cm / 30.48 )
# The program works fine now

# We can also use 2 function in the same line by incasing the "str" value into the float() function
# making one function the argument of another function
height_cm = float(input("Height converter: enter your height in cm: "))
print("Your height in feet is:", float_height_cm / 30.48 )

# Or you could use the int() function instead of float function
# The int() function turns a str input and converts it to an integer
year_born = int(input("What year were you born? "))
print("In 2100, you will be", 2100 - year_born, "years old, provided that you live this long!")

# You can also conver an interger or a float into a string using the str() function
# for example
temp_c = input("Enter the temperature today in the Celsius degrees: ")
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + " degrees Celsius equals " + str(temp_f) + " degrees Fahrenheit."
print(temp_statement)