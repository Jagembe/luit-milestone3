# Tuples in lists

city_1 = ("London", "UK", 8.98)
city_2 = ("Canberra", "Australia", 0.4)
city_3 = ("Algiers", "Algeria", 3.9)
capitals = [("London", "UK", 8.98), ("Canberra", "Australia", 0.4), ("Algiers", "Algeria", 3.9)]
for capital in capitals:
    print("Name:", capital[0], ", Country:", capital[1], ", Population:", capital[2])

# Lists in tuples
user_data = ("John", "American", 1964, [77.0, 78.2, 77.5]) # the list inside of this tuple is actually mutable
user_data[3].append(79.6) # adding an element to the list inside of the tuple 
print(user_data)


