#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 2 Summer 2022
# File:       Practice_02.py
# Purpose:    Calculate Groceries Prices
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

item1 = float(input('Enter price for item #1: '))
item2 = float(input('Enter price for item #2: '))
item3 = float(input('Enter price for item #3: '))
item4 = float(input('Enter price for item #4: '))
item5 = float(input('Enter price for item #5: '))

tax_rate = 0.06
subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * tax_rate
total = subtotal + tax

print()
print('Subtotal:', subtotal)
print('Tax:     ', tax)
print('Total:   ', total)
