# Define a dictionary to map English words to their German translations
sample_dict = {
    "mouth": "Mund",      # Mapping of "mouth" to "Mund"
    "finger": "Finger",   # Mapping of "finger" to "Finger"
    "leg": "Bein",        # Mapping of "leg" to "Bein"
    "hand": "Hand",       # Mapping of "hand" to "Hand"
    "face": "Gesicht",    # Mapping of "face" to "Gesicht"
    "nose": "Nase"        # Mapping of "nose" to "Nase"
}

# Start an infinite loop to continually prompt the user for input
while True:
    # Prompt the user for an English word or to exit
    user_input = input('Enter a word in English or EXIT: ').strip().lower()  # Strip whitespace and convert to lowercase
    
    # Check if the user wants to exit
    if user_input == 'exit':
        break  # Exit the loop and end the program
    
    # Check if the input word exists in the dictionary
    if user_input in sample_dict:
        # If the word exists, print its German translation
        print('Translation:', sample_dict[user_input])
    else:
        # If the word doesn't exist in the dictionary, inform the user
        print('No match!')
    

# Final message when the user exits
print('Bye!')

# Cool Feature: Adding new words to the dictionary
print("\nDo you want to add any words to the dictionary?")
new_word = input("Enter the English word (or type 'NO' to skip): ").strip().lower()

if new_word != 'no':
    new_translation = input(f"Enter the German translation for '{new_word}': ").strip()
    sample_dict[new_word] = new_translation  # Add the new word and its translation to the dictionary
    print(f"'{new_word}' has been added to the dictionary with the translation '{new_translation}'.")
else:
    print("No new words were added.")

# Display the final dictionary content
print("\nFinal dictionary contents:", sample_dict)
