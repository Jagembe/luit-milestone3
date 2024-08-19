# The pass instruction makes the code do nothing. If you remove pass the code will not run and will throw an error.
for i in range(11):
    pass

for a in range(1,6):
    for b in range(1, 6):
        print(a, "x", b, "=", a * b)

i = 2
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)