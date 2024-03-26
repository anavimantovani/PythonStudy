
def main():

    text = input('Enter some text: ')

    for position in range(0, len(text)):
        print('Position #' + str(position + 1) + ': ' + text[position], end='')

        if text[position].isdigit():
            print(' is a digit', end='')

        elif text[position].islower():
            print(' is lowercase', end='')

        elif text[position].isupper():
            print(' is uppercase', end='')

        elif text[position].isspace():
            print(' is a space', end='')


        print()


main()
