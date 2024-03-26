#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 12 Summer 2022
# File:       Practice_12.py
# Purpose:    Modify a string
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    print('Please enter some text:')  # Ask user to enter some text
    text = input()  # Prompt user for the text

    # Display the text backwards
    print()
    print(format('Backwards: ', '15s'), end='')

    # Foor loop to print the text backwards
    for position in range(len(text) - 1, -1, -1):
        print(text[position], end='')  # Print the text backwards

    print()  # Print a blank line

    total = 0  # Set variable so the loop can start

    # For loop so it counts the total digits
    for position_number in range(0, len(text)):

        # If the character on the string is a digit
        if text[position_number].isdigit():
            total = total + int(text[position_number])  # Add the digits

    print(format('Sum of digits: ', '15s') + str(total))  # Display the sum of digits

    print(format('Capitalized: ', '15s'), end='')  # Print capitalized header

    # Capitalize the first letter of each word
    for position_space in range(0, len(text)):

        # If the character before is a space
        if text[position_space - 1] == ' ' or position_space == 0:
            print(text[position_space].upper(), end='')  # Print the letter in uppercase

        # If the character before is not a space
        else:
            print(text[position_space].lower(), end='')  # Print the letter in lowercase

    print()  # Print a blank line


# Start the program
main()
