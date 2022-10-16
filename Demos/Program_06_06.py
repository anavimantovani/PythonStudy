


def main():
    first_age = int(input('Enter your age: '))
    second_age = int(input('Enter your best friend\'s age: '))

    # Chapter 2 way
    # total = first_age + second_age

    # Chapter 3 way
    # display_total(first_age, second_age)

    # total = sum_ages(first_age, second_age)

    # Chapter 6 - function procedures
    print()
    print('Together you are', sum_ages(first_age, second_age), 'years old.')


def sum_ages(age1, age2):
    result = age1 + age2
    return result


main()
