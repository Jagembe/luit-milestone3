# Assertions are assumptions in our program that should always be true.

def calculate_inverse(number):
    assert (number !=0), "Got 0 as number!"
    return 1 / number 

result = calculate_inverse(0)
print("The inverse is:", result)