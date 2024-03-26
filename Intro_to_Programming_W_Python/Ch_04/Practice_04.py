#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 4 Summer 2022
# File:       Practice_04.py
# Purpose:    Calculate amount of cents for a game
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

# Promp the user for the ammount of pennies, nickles, dimes and quarters
num_of_pennies = float(input('Enter number of pennies: '))
num_of_nickles = float(input('Enter number of nickles: '))
num_of_dimes = float(input('Enter number of dimes: '))
num_of_quarters = float(input('Enter number of quarters: '))

# Calculate how many cents were inserted
pennies_value = 1 * num_of_pennies
nickles_value = 5 * num_of_nickles
dimes_value = 10 * num_of_dimes
quarters_value = 25 * num_of_quarters

# Calculate the total money inserted
total = pennies_value + nickles_value + dimes_value + quarters_value

print() # Print a blank line

# If the user total 100 cents
if total == 100:
    print('You win!') # Tell the user they won
# If the user has more or less than 100 cents
else:
    print('Sorry, you have', total, 'cents.') # Tell the user the ammount they have


