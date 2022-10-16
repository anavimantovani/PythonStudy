
def main():
    menu_selection = 0

    while menu_selection != 4:
        menu_selection = display_menu()

        if menu_selection == 1:
            inches_to_centimeters()
        elif menu_selection == 2:
            feet_to_meters()
        elif menu_selection == 3:
            miles_to_kilometers()


def display_menu():
    print()
    print('1. - Convert inches to centimeters')
    print('2. - Convert feet to meters')
    print('3. - Convert miles to kilometers')
    print('4. - End the program')
    print()

    selection = int(input('Enter your selection: '))

    while selection < 1 or selection > 4:
        print()
        selection = int(input('That is an invalid selection. Enter 1, 2, 3 or 4: '))

    return selection


def inches_to_centimeters():
    print()
    inches = float(input('Enter the number of inches: '))

    centimeters = inches * 2.54

    print()
    print('That is equal to', centimeters, 'centimeters.' )
    print()


def feet_to_meters():
    print()
    feet = float(input('Enter the number of feet: '))

    meters = feet * 0.3048

    print()
    print('That is equal to', meters, 'meters.' )
    print()


def miles_to_kilometers():
    print()
    miles = float(input('Enter the number of miles: '))

    kilometers = miles * 1.609

    print()
    print('That is equal to', kilometers, 'kilometers.' )
    print()


main()
