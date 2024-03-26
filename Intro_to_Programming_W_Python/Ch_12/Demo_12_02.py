

def main():

    code_map = ['***'] * 128
    setup_array(code_map)

    text = ''

    while text.upper() != 'QUIT':
        print()
        print()
        print('Enter a message or QUIT when done:')

        text =  input()

        if text.upper() != 'QUIT':

            for position in range(0, len(text)):
                ascii_value = ord(text[position])

                if text[position] == ' ':
                    print()

                else:
                    print(code_map[ascii_value] + ' ', end='')

            print()


def setup_array(the_array):
    the_array[ord('A')] = '.-'
    the_array[ord('B')] = '-...'
    the_array[ord('C')] = '-.-.'
    the_array[ord('D')] = '-..'
    the_array[ord('E')] = '.'
    the_array[ord('F')] = '..-.'
    the_array[ord('G')] = '--.'
    the_array[ord('H')] = '....'
    the_array[ord('I')] = '..'
    the_array[ord('J')] = '.---'
    the_array[ord('K')] = '-.-'
    the_array[ord('L')] = '.-..'
    the_array[ord('M')] = '--'
    the_array[ord('N')] = '-.'
    the_array[ord('O')] = '---'
    the_array[ord('P')] = '.--.'
    the_array[ord('Q')] = '--.-'
    the_array[ord('R')] = '.-.'
    the_array[ord('S')] = '...'
    the_array[ord('T')] = '-'
    the_array[ord('U')] = '..-'
    the_array[ord('V')] = '...-'
    the_array[ord('W')] = '.--'
    the_array[ord('X')] = '-..-'
    the_array[ord('Y')] = '-.--'
    the_array[ord('Z')] = '--..'

    the_array[ord('a')] = '.-'
    the_array[ord('b')] = '-...'
    the_array[ord('c')] = '-.-.'
    the_array[ord('d')] = '-..'
    the_array[ord('e')] = '.'
    the_array[ord('f')] = '..-.'
    the_array[ord('g')] = '--.'
    the_array[ord('h')] = '....'
    the_array[ord('i')] = '..'
    the_array[ord('j')] = '.---'
    the_array[ord('k')] = '-.-'
    the_array[ord('l')] = '.-..'
    the_array[ord('m')] = '--'
    the_array[ord('n')] = '-.'
    the_array[ord('o')] = '---'
    the_array[ord('p')] = '.--.'
    the_array[ord('q')] = '--.-'
    the_array[ord('r')] = '.-.'
    the_array[ord('s')] = '...'
    the_array[ord('t')] = '-'
    the_array[ord('u')] = '..-'
    the_array[ord('v')] = '...-'
    the_array[ord('w')] = '.--'
    the_array[ord('x')] = '-..-'
    the_array[ord('y')] = '-.--'
    the_array[ord('z')] = '--..'

    the_array[ord('1')] = '.----'
    the_array[ord('2')] = '..---'
    the_array[ord('3')] = '...--'
    the_array[ord('4')] = '....-'
    the_array[ord('5')] = '.....'
    the_array[ord('6')] = '-....'
    the_array[ord('7')] = '--...'
    the_array[ord('8')] = '---..'
    the_array[ord('9')] = '----.'
    the_array[ord('0')] = '-----'

    the_array[ord(',')] = '--..--'
    the_array[ord('.')] = '.-.-.-'
    the_array[ord('?')] = '..--..'
    the_array[ord(';')] = '-.-.-'
    the_array[ord(':')] = '---...'
    the_array[ord('/')] = '-..-.'
    the_array[ord('-')] = '-....-'
    the_array[ord('(')] = '-.--.-'
    the_array[ord(')')] = '-.--.-'  # Note: same as '('
    the_array[ord('[')] = '-.--.-'  # Note: same as '('
    the_array[ord(']')] = '-.--.-'  # Note: same as '('
    the_array[ord('_')] = '..--.-'
    the_array[ord('"')] = '.-..-.'
    the_array[ord('=')] = '-...-'
    the_array[ord('\'')] = '.----.'  # Note: escaped apostrophe
    the_array[ord('/')] = '-..-.'
    the_array[ord('@')] = '.--.-.'


main()
