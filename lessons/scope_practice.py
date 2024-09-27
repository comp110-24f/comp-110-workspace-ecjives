def remove_chars (msg:str, char:str) -> str:
    copy:str = ""
    index:int = 0
    while (index < len(msg)):
        if (msg[index] != char):
            copy += msg[index]
        index += 1
    return copy

if __name__ == "__main__":
    message:str = "football"
    character:str = "o"
    print(remove_chars(message, character))