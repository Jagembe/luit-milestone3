# Define a function named 'print_letter_count' that takes two parameters:
# 'text' is the string to search within, and 'letter' is the letter to count (default is 'a').
def print_letter_count(text, letter="a"):
    """
    Counts the occurrences of a specified letter in the given text and prints the result.
    
    Parameters:
    text (str): The string in which to search for the letter.
    letter (str): The letter to count in the text. Default is 'a'.
    
    This function demonstrates how to use a for loop to iterate through a string,
    count occurrences of a character, and handle optional function arguments.
    """
    # Initialize a counter variable to keep track of the occurrences of 'letter'.
    counter = 0
    
    # Iterate over each character in the string 'text'.
    for char in text:
        # Check if the current character matches the 'letter' we're counting.
        if char == letter:
            # If it matches, increment the counter by 1.
            counter += 1
    
    # Print the result, showing how many times the 'letter' appeared in the 'text'.
    print("Number of", letter, "is", counter)

# Call the function to count the occurrences of 'a' in the string "avalanche".
print_letter_count("avalanche")

# --- Enhancements and Additional Examples ---

# 1. Case Sensitivity Handling
def print_letter_count_case_insensitive(text, letter="a"):
    """
    Counts the occurrences of a specified letter in the given text, case-insensitive, and prints the result.
    
    Parameters:
    text (str): The string in which to search for the letter.
    letter (str): The letter to count in the text. Default is 'a'.
    
    This function converts both the text and the letter to lowercase before counting,
    ensuring that the count is case-insensitive.
    """
    counter = 0
    # Convert both text and letter to lowercase for case-insensitive comparison
    text = text.lower()
    letter = letter.lower()
    
    for char in text:
        if char == letter:
            counter += 1
    
    print(f"Number of '{letter}' is {counter}")

# Call the case-insensitive version of the function
print_letter_count_case_insensitive("Avalanche")

# 2. Counting Multiple Letters at Once
def print_multiple_letter_counts(text, letters):
    """
    Counts the occurrences of multiple specified letters in the given text and prints the results.
    
    Parameters:
    text (str): The string in which to search for the letters.
    letters (str): A string containing the letters to count in the text.
    
    This function iterates over each letter in 'letters' and counts its occurrences in 'text'.
    """
    # Use a dictionary to store the counts of each letter
    letter_counts = {}
    
    # Initialize the count for each letter in the 'letters' string
    for letter in letters:
        letter_counts[letter] = 0
    
    # Iterate over each character in the text
    for char in text:
        # Check if the current character is in the 'letters' string
        if char in letters:
            # Increment the count for that letter
            letter_counts[char] += 1
    
    # Print the results for each letter
    for letter, count in letter_counts.items():
        print(f"Number of '{letter}' is {count}")

# Call the function to count multiple letters in the string "avalanche"
print_multiple_letter_counts("avalanche", "ae")
