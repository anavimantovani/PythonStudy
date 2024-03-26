
def main():
    print('\n*** James Show ***\n')

    starting_message()
    step1()
    step2()
    step3()
    step4()


def starting_message():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer')
    print('There are four steps in this process')

    pause_message(1)


def step1():
    print('Step #1: Unplug the dryer and')
    print('move it away from the wall.')

    pause_message(2)


def step2():
    print('Step #2: Remove the six screws')
    print('from the back of the dryer.')

    pause_message(3)


def step3():
    print('Step #3: Remove the dryer\'s')
    print('back panel.')

    pause_message(4)


def step4():
    print('Step #4: Pull the top of the')
    print('dryer straight up.')


def pause_message(step_number):
    print()
    xyz = input('Press <Enter> to see Step #' + str(step_number) + ': ')
    print()
    print()


main()
