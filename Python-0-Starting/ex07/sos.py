import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", 
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", 
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", 
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", 
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", 
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", 
    "8": "---..", "9": "----."
}


def checker(str):
    '''check if the str is only in alpha'''
    try:
        i = 0
        for lettre in str:
            if lettre.isalpha():
                i += 1
            if not lettre.isalpha():
                i = 0
                raise AssertionError("AssertionError: the argument are bad")
    except AssertionError as e:
        print(e)

    return i


def ft_morse(str):
    '''Morse fonction that translate str to morse'''
    try:
        if checker(str) != 0:
            morse_list = [NESTED_MORSE[char.upper()] for char in str]
            print(' '.join(morse_list))

    except AssertionError as e:
        print(e)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: wrong number of arguments")
        str = sys.argv[1]
        ft_morse(str)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
