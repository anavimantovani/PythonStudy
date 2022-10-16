

def main():
    print('\n*** James Show ***\n')

    number = int(input('Enter a number and I will display it doubled: '))

    double_number(number)


def double_number(value):
    result = value * 2
    print(result)


main()
