# Assertions are assumptions in our program that should always be true.
# USE assertions for debugging/testing your code & for documenting your code.
# You can use assertions as "sanity checks" at the beginning of a function to make sure it recieves correct data.
# DO NOT validate user inputs with assertions or handle AsseretionErrors in try...except
# Assersions are not an error handling tool. They are used to catch bugs during testing

def calculate_inverse(number):
    assert (number !=0), "Got 0 as number!"
    return 1 / number 

result = calculate_inverse(0)
print("The inverse is:", result)