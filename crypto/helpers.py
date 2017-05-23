import string

def alphabet_position(letter):
    lower_letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(lower_letter)

def rotate_character(char, rot):
    if str(char) in string.digits:
        return char
    elif str(char) in string.punctuation or str(char) in string.digits:
        return char
    elif char == char.lower():
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        idx = (alphabet_position(char) + rot) % 26
        new_char = alphabet[idx]
        return new_char   
    elif char == char.upper():
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = (alphabet_position(char) + rot) % 26
        new_char = alphabet_upper[idx]
        return new_char