#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Project 01 Summer 2022
# File:       Project_01.py
# Purpose:    Calculate the factorial of a number
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

integer = int(input('Enter an integer greater than 1: '))  # Prompt the user for an integer greater than 1
total = 1  # Set variable to 1 so the loop can start

# Display the number given by the user in factorial notation and an equal sign
print()
print(str(integer) + '! ' + '= ', end='')

# Perform the loop the amount of times between 1 and the integer
for counter in range(1, integer + 1):
    # If counter is less than the integer
    if counter < integer:
        print(counter, 'x ', end='')  # Display the counter followed by an 'x'

    # If counter is equal to the integer
    if counter == integer:
        print(counter, end='')  # Display only the counter

    total *= counter  # Multiply all the numbers in range

print(' =', total)  # Print the equal sign and the product of the multiplication

