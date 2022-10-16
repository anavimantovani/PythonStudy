#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Program 05 01 Summer 2022
# File:       Program_05_01.py
# Purpose:    Commission calculator
#######################################################

# Percentage of each sale that is the salesperson's commission
COMMISSION_RATE = 0.08

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

# Display a welcome message to the user
print()
print('Welcome to the commission calculator program!')
print()

keep_going = 'y'  # Set variable to 'y' so loop executes the first time

# Do as many calculations as the user would like to
while keep_going == 'y':
    # Prompt the user for the sales amount
    print()
    sales = float(input('Enter the amount of sales: '))

    # Calculate the salesperson's commission based on the fixed percentage
    commission = sales * COMMISSION_RATE

    # Display the commission to the user
    print()
    print('The commission is $' + str(commission))
    print()

    # Ask if the user wants to make another calculation
    keep_going = input('Do you want to calculate another commission (y/n)? ')

# Display the ending thank you message
print()
print('Thank you for using the commission calculator program.')
