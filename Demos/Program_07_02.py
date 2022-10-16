

def main():

    do_another = 'y'

    while do_another == 'y':

        show_retail()

        print()
        do_another = input('Do you have another item (y/n)?')


def show_retail():

    print()
    wholesale = float(input('Enter an item\'s wholesale cost: '))

    while wholesale <= 0:
        print()
        print('Error, the price must be greater than zero.')
        print()

        wholesale = float(input('Please, re-enter an item\'s wholesale cost: '))

    retail = round(wholesale * 2.5, 2)

    print()
    print('The retail price is $' + format(retail,'.2f'))
    print()

main()
