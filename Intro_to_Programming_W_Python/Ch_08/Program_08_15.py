
SIZE = 6

def main():
    names = [''] * SIZE
    hours = [0.0] * SIZE

    for counter in range(0, SIZE):
        names[counter] = input('Enter the name of employee #' + str(counter + 1) + ': ')
        hours[counter] = float(input('Enter the hours worked by ' + names[counter] + ': '))
        print()

    pay_rate = float(input('Enter the hourly pay rate: '))

    print()
    print()

    for counter in range(0, SIZE):
        gross_pay = round(pay_rate * hours[counter], 2)

        print(format(names[counter], '10s') + ' : $', end='')
        print(format(gross_pay, '8,.2F'))



main()
