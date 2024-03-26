#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 7 Summer 2022
# File:       Practice_07.py
# Purpose:    Calculate the Gross Pay
####################################################### 

MIN_HOUR_WORKED = 0  # Declare global constant for the min of hours worked
MAX_HOUR_WORKED = 40  # Declare global constant for the max of hours worked
MIN_HOURLY_PAY = 7.5  # Declare global constant for the min of hourly pay
MAX_HOURLY_PAY = 18.25  # Declare global constant for the max of hourly pay

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    hours = get_hours()  # Call the function to prompt user for the hours worked
    rate = get_rate()  # Call the function to prompt user for the hourly pay

    gross_pay = hours * rate  # Calculate the gross pay

    # Display the Gross Pay
    print()
    print('Gross Pay:', format(gross_pay, ',.2f'))


# Prompt user for a valid number of hours worked
def get_hours():

    # Prompt user for the number of hours worked
    num_of_hours = float(input('Enter the number of hours worked: '))

    # While number of hours worked is less than 0 or more than 40
    while num_of_hours <= MIN_HOUR_WORKED or num_of_hours >= MAX_HOUR_WORKED:

        # Display an error message to the user
        print()
        print('ERROR - Invalid number of hours!')
        print()

        # Ask the user to enter the number again
        num_of_hours = float(input('Enter the number of hours worked: '))

    return num_of_hours  # Return the number of hours worked to the main module


# Prompt user for a valid hourly rate
def get_rate():

    # Prompt user for the hourly rate
    print()
    print()
    hour_rate = float(input('Enter hourly rate: '))

    # While the hourly rate is less than 7.5 or more than 18.25
    while hour_rate <= MIN_HOURLY_PAY or hour_rate >= MAX_HOURLY_PAY:

        # Display an error message to the user
        print()
        print('ERROR - Invalid number of hourly rate!')
        print()

        # Ask the user to enter the hourly rate again
        hour_rate = float(input('Enter hourly rate: '))

    return hour_rate  # Return the hourly rate to the main module


# Start the program
main()
