#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 03 Summer 2022
# File:       Homework_03.py
# Purpose:    Body Mass Index Calculator
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    weight_user = float(input('Pounds: '))  # Prompt user for their weight
    height_feet = float(input('Feet: '))  # Prompt user for their height in feet
    height_inches = float(input('Inches: '))  # Prompt user for their height in inches

    # Display the results to the user
    display_results(weight_user, height_feet, height_inches)


# Display the results to the user
def display_results(weight, feet, inches):
    total_inches = feet * 12 + inches  # Calculate the total height in inches
    bmi_total = weight * 703 / total_inches ** 2  # Calculate the BMI

    # Display the result to the user
    print()
    print('Your BMI is', bmi_total)


# Start the program
main()
