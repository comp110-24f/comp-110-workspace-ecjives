from random import random
from random import choice

print("Hello World")
print(1_000_000 + 1_000)
print("spooky season"[2 + 2])
print(True)

for attempts in range(3):

    print(random())
    print(choice("wxyz"))

def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"
    
print(check_first_letter(word="happy", letter="h"))
