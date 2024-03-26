#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 4 Summer 2022
# File:       Homework_04.py
# Purpose:    Calculate the amount of seconds in minutes, hours and days
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

# Prompt the user for the amount of seconds
num_of_seconds = int(input('Enter the number of seconds: '))

# Calculate the amount of seconds in minutes, hours and days
num_of_minutes = num_of_seconds / 60
num_of_hours = num_of_minutes / 60
num_of_days = num_of_hours / 24

print() # Print a blank line

# If number of seconds is bigger or equal to 60 and smaller than 3600
if num_of_seconds >= 60 and num_of_seconds < 3600:
    # Tell the user how many minutes there is in that amount of seconds
    print(num_of_seconds, 'seconds is equal to', num_of_minutes, 'minutes.')

# If number of seconds is bigger or equal to 3600 and smaller than 86400
elif num_of_seconds >= 3600 and num_of_seconds < 86400:
    # Tell the user how many hours there is in that amount of seconds
    print(num_of_seconds, 'seconds is equal to', num_of_hours, 'hours.')

# If number of seconds is bigger or equal to 86400
elif num_of_seconds >= 86400:
    # Tell the user how many days there is in that amount of seconds
    print(num_of_seconds, 'seconds is equal to', num_of_days, 'days.')

# If the user entered a number of seconds smaller than 60
else:
    print() # Display no message
