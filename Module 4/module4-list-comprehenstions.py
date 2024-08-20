# list comprehensions
# what if you need to create a really long list?

numbers = [i for i in range(1, 101)]
print(numbers) # printing number from 1 to 100

numbers = [i for i in range(1, 101) if i % 3 != 0] # excluding numbers that are divisible by 3 from the list different from 0
print(numbers) 