#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 2 Summer 2022
# File:       Program_04_01.py
# Purpose:    Grade calculator
#######################################################

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

# Prompt the user for three test scores
test1 = float(input('Enter test score #1: '))
test2 = float(input('Enter test score #2: '))
test3 = float(input('Enter test score #3: '))

# Calculate the avarage test score
average = (test1 + test2 + test3) / 3

# Display the avarage of the user
print()
print('Your average is', average)
print()

# If the users avarage is 95% or higher
if average >= 95:
    print('That is a great average!!!') # Tell the user that they are great
# If the users avarage is 80% or higher
elif average >= 80:
    print('That is a good average!') # Tell the user that they are good
# If the user avarage is 70% or higher
elif average >= 70:
    print('That is an average average.') # Tell the user that they are avarage
# If the user avarage is less than 70%
else:
    print('That is not a good average.') # Tell the user that they are struggling
