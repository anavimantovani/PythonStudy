#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 05 Summer 2022
# File:       Homework_05.py
# Purpose:    Conversion chart for Celsius to Fahrenheit
####################################################### 

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

celcius = -15.0  # Set variable to 15.0 so the loop can start
fahrenheit = 0  # Set variable to 0 so the loop can start and not affect the calculation

# Calculate from -15 to 40 degrees Celsius in 2.5 degrees increment the equivalent in Fahrenheit
while celcius <= 40:

    fahrenheit = 1.8 * celcius + 32  # Calculate the equivalent of Celsius in Fahrenheit
    # Display what the temperature in Celsius is equal to in Fahrenheit
    print(celcius, 'degrees Celsius is', fahrenheit, 'degrees Fahrenheit.')

    celcius += 2.5  # Add 2.5 degrees to the temperature in Celsius
