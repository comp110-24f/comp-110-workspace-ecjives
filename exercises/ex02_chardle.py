"""9/13/24 - Chardle Exercise"""

__author__ = "730745467"

def input_word() -> str:
    inputted_word: str = input("Enter a 5-character word: ") # Provide a word to check
    if (len(inputted_word) == 5): # If there are 5 letters, return it
        return inputted_word
    else: # Else, give an error and end the program
        print("Error: Word must contain 5 characters.")
        exit()
def input_letter() -> str: 
    inputted_letter: str = input("Enter a single character: ") # Provide a letter to check
    if (len(inputted_letter) == 1): # If there is 1 letter, return it
        return inputted_letter
    else: # Else, give an error and end the program
        print("Error: Character must be a single character.")
        exit()
def contains_char(inputted_word: str, inputted_letter: str) -> None: # Checks each index of the word for a matching letter, returns a print statement if there is
    print("Searching for " + inputted_letter + " in " + inputted_word)
    matching_count: int = 0 # Initialize count
    if (inputted_word[0] == inputted_letter): # Ineffcient, but effective
        print(inputted_letter + " found at index 0")
        matching_count += 1
    if (inputted_word[1] == inputted_letter):
        print(inputted_letter + " found at index 1")
        matching_count += 1
    if (inputted_word[2] == inputted_letter):
        print(inputted_letter + " found at index 2")
        matching_count += 1
    if (inputted_word[3] == inputted_letter):
        print(inputted_letter + " found at index 3")
        matching_count += 1
    if (inputted_word[4] == inputted_letter):
        print(inputted_letter + " found at index 4")
        matching_count += 1
    
    if (matching_count == 0):
        print("No instances of " + inputted_letter + " found in " + inputted_word) # Returns the number of matching letters in the word
    elif (matching_count == 1):
        print(str(matching_count) + " instance of " + inputted_letter + " found in " + inputted_word)
    else:
        print(str(matching_count) + " instances of " + inputted_letter + " found in " + inputted_word)
def main() -> None: # Run all of the functions together
    word: str = input_word() # Set a word
    letter: str = input_letter() # Set a letter
    contains_char(word, letter) # Use the set word and letter to count

if __name__ == "__main__":
    main()