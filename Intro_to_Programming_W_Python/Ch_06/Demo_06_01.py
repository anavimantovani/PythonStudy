#####
#
#####

import math

def main():
    #print de nome

    # String Functions
    example_string = 'Hello world!'
    print(example_string)
    print(len(example_string))
    print(example_string.upper())
    print(example_string.lower())
    print(example_string.replace('o', '*'))
    example_string = example_string + '!!'
    print(example_string)
    print(example_string.find('W'))
    print(example_string.find('w'))

    if example_string.find('w') != -1:
        print('It has a "w"')
    else:
        print('No "w"')

    #substring
    print(example_string[2:8])

    print('---------------------')

    # transform string value to another data type
    example = '3453.345000'
    example_float = float(example)
    #example_float = example_float + 1
    print(example)
    print(example_float)

    print('---------------------')

    #example_float = math.sin(90 * math.pi / 180)
    example_float = math.sin(math.radians(90))
    print(example_float)

    print('---------------------')

    # Square root
    example_int = 64
    print(math.sqrt(example_int))

    print('---------------------')

    # round numbers
    example_float1 = 32.2345
    example_float2 = 3456.9832

    print(round(example_float1))
    print(round(example_float1, 0))
    print(round(example_float1, 2))
    print(round(example_float1, 3))

    print()

    print(round(example_float2))
    print(round(example_float2, 0))
    print(round(example_float2, 2))
    print(round(example_float2, 3))


main()
