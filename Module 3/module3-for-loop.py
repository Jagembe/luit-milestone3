# for loops

for letter in "hello!":
    print("Current letters:", letter)

# here is the while loop from the previous lesson (compare this with the for loop)
counter = 1
while counter < 11:
    print(counter)
    counter += 1
print("Finished!")

# in this for loop here we see it takes less code than the "while loop"
# the first value after range is 1 and it is inclusive. The 11 value is exclusive meaning it won't print since it is the stopping point
for counter in range(1,11):
    print(counter)
print("Finished!")
# this is only one of the 3 versions of the range value. Let's look at the other two.

# The 11 value is defined as the stoppoing value. Python will auto include the 0 as the starting point ex: 0, 1, 2, 3...10.
# Python knows to treat a single value in a range as the exclusive stopping point and 0 as the start point if not defined.
for counter in range(11):
    print(counter)
print("Finished!")

# This range will count ever second number ex: 1, 3, 5, 7, 9.
for counter in range(1, 11, 2):
    print(counter)
print("Finished!")