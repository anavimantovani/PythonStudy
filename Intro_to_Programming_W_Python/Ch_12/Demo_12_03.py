
def main():

    text = 'abc'

    while text != '':
        print('Enter a message:')
        text = input()

        if len(text) != 0:
            print(encode_string(text))

        print()
        print()


def encode_string(orig_string):
    upper_string = orig_string.upper()
    out = ''

    for position in range(0, len(orig_string)):
        ascii_value = ord(orig_string[position])

        # Character is first half of the alphabet
        #if ascii_value >= 65 and ascii_value <= 77 or ascii_value >= 97 and ascii_value <= 109:
        if upper_string[position] >= 'A' and upper_string[position] <= 'M':
            out = out + chr(ascii_value + 13)

        #elif ascii_value >= 78 and ascii_value <= 90 or ascii_value >= 110 and ascii_value <= 122:
        elif upper_string[position] >= 'N' and upper_string[position] <= 'Z':
            out = out + chr(ascii_value - 13)

        else:
            out = out + chr(ascii_value)

    return out


main()
