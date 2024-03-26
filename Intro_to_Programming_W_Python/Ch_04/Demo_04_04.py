
num1 = float(input('Enter a number: ')
num2 = float(input('Enter a different number: '))

num1_first = num1 < num2
num2_first = not num1_first

print()

if num1_first:
    print('The first number is smaller than the second')

if num2_first:
    print('The second number is smaller than the first')
