"""9/13/24 - Chardle Exercise"""

__author__ = "730745467"

def input_word() -> str:
# Provide a string to check
# If there are 5 characters in the string, return it
# Else, give an error and end the function
    inputted_word: str = input("Enter a 5-character word: ")
    if (len(inputted_word) == 5):
        return inputted_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()

def input_letter() -> str:
# Provide a string to check
# If there is 1 character in the string, return it
# Else, give an error and end the function
    inputted_letter: str = input("Enter a single character: ")
    if (len(inputted_letter) == 1):
        return inputted_letter
    else:
        print("Error: Character must be a single character.")
        exit()

def contains_char(inputted_word: str, inputted_letter: str) -> None:
# Check each index of the word for a matching letter
    print("Searching for " + inputted_letter + " in " + inputted_word)
    matching_count: int = 0
# Print statement and initialize count
    if (inputted_word[0] == inputted_letter):
        print(inputted_letter + " found at index 0")
        matching_count += 1
# Checks the index for a match
# If there's a match, add 1 to the count
# Repeat for all 5 letters in the word
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
# Provides a different string depending on if there's 0, 1, or 2+ matches
        print("No instances of " + inputted_letter + " found in " + inputted_word)
    elif (matching_count == 1):
        print(str(matching_count) + " instance of " + inputted_letter + " found in " + inputted_word)
    else:
        print(str(matching_count) + " instances of " + inputted_letter + " found in " + inputted_word)

def main() -> None:
# Run all of the functions together
# Sets a word and checks it
# Sets a letter and checks it
# Use the set word and letter from before to count the number of matches
    word: str = input_word()
    letter: str = input_letter()
    contains_char(word, letter)

if __name__ == "__main__":
# Run the function from start
    main()