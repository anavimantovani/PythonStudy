
SIZE = 6

def main():
    hours = [0.0] * SIZE

    for counter in range(0, SIZE):
        hours[counter] = float(input('Enter number of hours worked by employee #' + str(counter + 1) + ': '))

    print()
    pay_rate = float(input('Enter the hourly pay rate: '))

    print()
    print()

    for counter in range(0, SIZE):
        gross_pay = round(pay_rate * hours[counter], 2)

        print('Employee # ' + str(counter + 1) + ': $' + format(gross_pay, '8,.2F'))


main()
