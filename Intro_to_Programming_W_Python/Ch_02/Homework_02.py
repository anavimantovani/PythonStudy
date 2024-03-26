#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 2 Summer 2022
# File:       Homework_02.py
# Purpose:    Calculate Property Area in Acres
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

length = float(input('Enter the length of the property in feet: '))
width = float(input('Enter the width of the property in feet: '))

area = width * length / 43560

print()
print('The property is', area, 'acres!')
