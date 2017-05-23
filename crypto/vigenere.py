from helpers import alphabet_position, rotate_character
import string

def encrypt(text, code):
    encrypted = ''
    code_start = 0
    for char in text:
        if char == ' ':
            encrypted += ' '
        elif char in string.punctuation or char in string.digits:
            encrypted += char
        else:
            if code_start < len(code):
                rot = alphabet_position(code[code_start])
                encrypted += rotate_character(char, rot)
                code_start += 1
            else:
                code_start = 0
                rot = alphabet_position(code[code_start])
                encrypted += rotate_character(char, rot)
                code_start += 1
                
    return encrypted

def main():
    text = input("Type a message: ")
    code = input("Code Word: ")
    print(encrypt(text, code))

if __name__ == "__main__":
    main()
    