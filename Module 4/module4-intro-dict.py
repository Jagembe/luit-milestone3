# Dictionaries
# A dictionary to store email addresses with people's names as keys.
# Each key (person's name) is associated with a unique email address.
emails = {
    "Anne Stahl": "astahl@gmail.com",   # Key: "Anne Stahl", Value: "astahl@gmail.com"
    "Peter Small": "peters@yndex.com",  # Key: "Peter Small", Value: "peters@yndex.com"
    "Mark Steel": "mark@steel.com"      # Key: "Mark Steel", Value: "mark@steel.com"
}

# Accessing the value associated with the key "Mark Steel" and printing it.
# This will print: mark@steel.com
print(emails["Mark Steel"])

# Adding a new email entry to the dictionary.
emails["John Doe"] = "johndoe@example.com"  # Adding John Doe's email

# Updating an existing email entry for Mark Steel.
emails["Mark Steel"] = "mark.new@steel.com"  # Updating Mark Steel's email

# Removing Peter Small's email entry from the dictionary.
del emails["Peter Small"]  # Deletes Peter Small's entry

# Checking if "Anne Stahl" exists in the dictionary before accessing her email.
if "Anne Stahl" in emails:
    print("Anne's email is:", emails["Anne Stahl"])

# Attempting to access a non-existent key using 'get' with a default value.
# This will print: Email not found
print(emails.get("Unknown Person", "Email not found"))

# Looping through the dictionary to print each name and corresponding email.
for name, email in emails.items():
    print(f"{name}: {email}")  # Prints each name and email

# Merging another dictionary with additional emails into the 'emails' dictionary.
more_emails = {
    "Jane Doe": "jane.doe@example.com",  # New email entry for Jane Doe
    "Alice White": "alice@white.com"     # New email entry for Alice White
}
emails.update(more_emails)  # Adds new entries to the 'emails' dictionary

# Printing the updated dictionary after merging.
print("Updated emails dictionary:")
for name, email in emails.items():
    print(f"{name}: {email}")  # Prints each name and email


# A dictionary to store English animal names as keys and their Spanish equivalents as values.
spanish_animals = {
    "dog": "el perro",          # Key: "dog", Value: "el perro" (Spanish translation for dog)
    "cat": "el gato",           # Key: "cat", Value: "el gato" (Spanish translation for cat)
    "horse": "el caballo",      # Key: "horse", Value: "el caballo" (Spanish translation for horse)
    "bird": "el pájaro"         # Key: "bird", Value: "el pájaro" (Spanish translation for bird)
}

# Accessing the value associated with the key "bird" and printing it.
# This will print: el pájaro
print(spanish_animals["bird"])

# Note: In dictionaries, each key must be unique. 
# If you try to create a dictionary with duplicate keys, the last key-value pair will overwrite the previous one.


# A dictionary where the keys are city names, and the values are lists of ratings given by different users.
city_ratings = {
    "Bangkok": [7, 4, 7, 5],    # Key: "Bangkok", Value: [7, 4, 7, 5] (List of ratings for Bangkok)
    "Hanoi": [7, 6, 4, 5],      # Key: "Hanoi", Value: [7, 6, 4, 5] (List of ratings for Hanoi)
    "Manila": [6, 6, 4, 4, 5]   # Key: "Manila", Value: [6, 6, 4, 4, 5] (List of ratings for Manila)
}

# Accessing the list of ratings associated with the key "Hanoi" and printing it.
# This will print: [7, 6, 4, 5]
print(city_ratings["Hanoi"])

# Get the list of ratings for Hanoi
hanoi_ratings = city_ratings["Hanoi"]

# Calculate the average by summing the ratings and dividing by the number of ratings
average_hanoi_rating = sum(hanoi_ratings) / len(hanoi_ratings)

# Print the average rating
# This will print: The average rating for Hanoi is: 5.5
print("The average rating for Hanoi is:", average_hanoi_rating)

# Adding a new city with ratings
city_ratings["Tokyo"] = [8, 7, 9, 6]  # New ratings for Tokyo

# Updating ratings for an existing city
city_ratings["Bangkok"] = [8, 5, 7]   # Updated ratings for Bangkok

# Deleting a city's ratings
del city_ratings["Manila"]  # Deletes Manila's ratings

# Looping through the dictionary to print each city and its average rating.
print("City ratings and their averages:")
for city, ratings in city_ratings.items():
    avg_rating = sum(ratings) / len(ratings)
    print(f"{city}: Average rating = {avg_rating:.2f}")  # Prints each city and its average rating
