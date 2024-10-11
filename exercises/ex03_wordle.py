"""9/25/24 - Wordle Exercise"""

__author__ = "730745467"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Set the emojis

def input_guess (secret_len:int) -> str:
# Asks for a guess
# If the guess is not the appropriate length, it keeps asking
# Return the guess if/when it's the appropriate length
    word_guess:str = input(f"Enter a {secret_len} character word: ")
    while (len(word_guess) != secret_len):
        word_guess = input(f"That wasn't {secret_len} chars! Try again: ")
    return word_guess

def contains_char (secret_word:str, letter:str) -> bool:
# Checks to see if the given string for "letter" is only one character
# Checks each index of the secret word for a match with "letter"
# Returns True if it finds one, False if not
    assert len(letter) == 1
    index:int = 0
    while (index < len(secret_word)):
        if (secret_word[index] == letter):
            return True
        index += 1
    return False

def emojified (guessed_word:str, secret_word:str) -> str:
# Checks to be sure the secret word and guessed word have equal length
# Runs through each index of both the secret and guess
# If both words have the same letter at the same index, add a green box to the final answer
# Else, run the contains_char funcrion, and if true, add a green box to the final answer
# If neither is true, add a white box to the final answer
# Return the final response
    assert len(secret_word) == len(guessed_word)
    index:int = 0
    final_response:str = ""
    while (index < len(secret_word)):
        if (secret_word[index] == guessed_word[index]):
            final_response += GREEN_BOX
        elif (contains_char(secret_word, guessed_word[index])):
            final_response += YELLOW_BOX
        else:
            final_response += WHITE_BOX
        index += 1
    return final_response

def main(secret: str) -> None:
# For 6 turns, run the emojified function
# If the final response is nothing but green boxes, the player has won
# If the player doesn't guess in 6 turns, the player has lost
    turns:int = 1
    while (turns <= 6):
        print(f"=== Turn {turns}/6 ===")
        wordle:str = emojified(secret, input_guess(len(secret)))
        print(wordle)
        if (wordle == (GREEN_BOX * len(secret))):
            print(f"You won in {turns}/6 turns!")
            return None
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="codes")
