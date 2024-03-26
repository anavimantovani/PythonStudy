#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 5a Summer 2022
# File:       Practice_05a.py
# Purpose:    Calculate the sum of numbers entered
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

enter_number = 9999  # Set variable to 9999 so the loop can start
total = 0  # Set variable to 0 so loop can start and not affect the sum

# Enter as much numbers as the user would like to
while enter_number != 0:
    # Ask the user for a positive number
    enter_number = float(input('Enter a positive number (or zero when done): '))

    total = total + enter_number  # Calculate all the numbers entered

# Display the sum of the numbers entered
print()
print('Sum:', total)
