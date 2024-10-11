"""9/27/24 - Variables, Scope, and Importing Functions Challenge Question"""

__author__ = "730745467"

def concat (first_word:str, second_word:str) -> str:
    return (first_word + second_word)

word1:str = "happy"
word2:str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))