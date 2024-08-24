input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

sum = 0.0 
for number in input_numbers:
    sum += number
average = sum / len(input_numbers)

print(average)
# Now lets turn the code above into a function

def get_agerage(input_numbers):
    sum = 0.0 
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

get_agerage([5.0, 3.5, 7.8, 9.9, 10.0])

# Lets make a function that has 2 parameters now

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print("Number of", letter, "is", counter)

print_letter_count("Welcome", "e")

print_letter_count("Yesterday I went to buy groceries in the morning", "o")
