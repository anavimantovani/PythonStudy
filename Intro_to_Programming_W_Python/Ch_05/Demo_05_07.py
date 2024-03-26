number1 = -9999

while number1 != -1:
    number1 = int(input('Enter a number greater than zero (or -1 to exit): '))

    if  number1 != -1:
        number2 = int(input('Enter a different number greater than zero: '))

        if number1 > number2:
            print('The first number is greater than the second.')
        else:
            print('The second number is greater than the second.')

print()
print()
