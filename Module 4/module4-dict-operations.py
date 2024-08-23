# Dictionary Operations

grades = {}
grades["John"] = "A-"
grades["Anne"] = "B"
print(grades)

grades["Anne"] = "A"
print(grades)
# or
grades.update({"John":"A+"})
print("Updated Grades:", grades)

# Checking the number of key values in a dictionary
print(len(grades))

# To check if a given key is present in a dict
if "John" in grades:
    print("John got:", grades["John"])

#del grades["John"]
#print(grades)

# Acces to the keys in dictionaries
for el in grades.keys():
    print(el)

# Access to the values in dictionaries
for el in grades.values():
    print(grades)

# Access to both keys and values
for person, grade in grades.items():
    print(person, "got", grade)

