import sys


def ft_check_str(str):
    '''This function counts the number of characters in a string'''
    try:
        counter = 0
        alpha = 0
        digit = 0
        space = 0
        uppercase = 0
        ponctuation = 0
        for i in str:
            if i.isalpha():
                alpha += 1
            if i.isdigit():
                digit += 1
            if i.isspace() or i == "/n":
                space += 1
            if i.isupper():
                uppercase += 1
            if i in ["!", "?", ".", ",", ";", ":", "'", '"', "-"]:
                ponctuation += 1
            counter += 1
        print(f"The text contains {counter} characters:")
        print(f"{uppercase} upper letters")
        print(f"{alpha - uppercase} lower letters")
        print(f"{ponctuation} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except ValueError:
        raise AssertionError("AssertionError: argument is not a string")


def main():
    try:
        if len(sys.argv) == 2:  # Si un argument est fourni
            text = sys.argv[1]
        elif len(sys.argv) == 1:  # Si aucun argument n'est fourni
            text = input("What is the text to count?\n")
        else:  # Si plus d'un argument est fourni
            raise AssertionError("more than one argument is provided")
        ft_check_str(text)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
