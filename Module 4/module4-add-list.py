# Adding new elements to lists

# Initialize a list of book ratings with five integer values
book_ratings = [7, 9, 5, 6, 8]

# Append a new rating (4) to the end of the book_ratings list
book_ratings.append(4)
# Print the updated list after appending
# The list now contains: [7, 9, 5, 6, 8, 4]
print(book_ratings)

# The following line does nothing since book_ratings is not being assigned or printed
# Simply stating 'book_ratings' in a script has no effect; this line can be removed without impact
book_ratings

# Insert a new rating (10) at index 1 in the book_ratings list
# This shifts all the elements after index 1 to the right
book_ratings.insert(1, 10)
# Print the updated list after insertion
# The list now contains: [7, 10, 9, 5, 6, 8, 4]
print(book_ratings)
