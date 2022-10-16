#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Project 02 Summer 2022
# File:       Project_02.py
# Purpose:    Transform a string into a phone number
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    user_text = 'abc'  # Initialize variable so the loop can start

    # While the user doesn't press ENTER
    while user_text != '':

        upper_counter = 0  # Set counter to zero
        lower_counter = 0  # Set counter to zero

        print()  # Display a blank line
        print()  # Display a blank line
        print('Please enter some text or press <ENTER> to exit:')  # Ask user for a text

        user_text = input()  # User's input text

        print()  # Display a blank line

        # If the user didn't press ENTER
        if user_text != '':

            # Go over every position of the string
            for position in range(0, len(user_text)):

                # Get the ASCII value of the character
                ascii_value = ord(user_text[position])

                # If the ASCII value is among the uppercase letters
                if ascii_value >= 65 and ascii_value <= 90:
                    upper_counter += 1  # Add to the counter of uppercase characters

                # If the ASCII value is among the lowercase letters
                elif ascii_value >= 97 and ascii_value <= 122:
                    lower_counter += 1  # Add to the counter of lowercase characters

            print('Lower case:           ' + str(lower_counter))  # Total of lowercase characters
            print('Upper case:           ' + str(upper_counter))  # Total of uppercase characters
            print('Telephone:            ', end='')  # Display the string as a telephone number

            user_text_upper = user_text.upper()  # Make the string uppercase

            # Go over every position of the string
            for position in range(0, len(user_text_upper)):

                # Get the ASCII value of the character
                ascii_value = ord(user_text_upper[position])

                # If the ASCII value is 65, 66 or 67
                if ascii_value >= 65 and ascii_value <= 67:
                    print('2', end='')  # Print the number 2

                # If the ASCII value is 68, 69 or 70
                elif ascii_value >= 68 and ascii_value <= 70:
                    print('3', end='')  # Print the number 3

                # If the ASCII value is 71, 72 or 73
                elif ascii_value >= 71 and ascii_value <= 73:
                    print('4', end='')  # Print the number 4

                # If the ASCII value is 74, 75 or 76
                elif ascii_value >= 74 and ascii_value <= 76:
                    print('5', end='')  # Print the number 5

                # If the ASCII value is 77, 78 or 79
                elif ascii_value >= 77 and ascii_value <= 79:
                    print('6', end='')  # Print the number 6

                # If the ASCII value is 80, 81, 82 or 83
                elif ascii_value >= 80 and ascii_value <= 83:
                    print('7', end='')  # Print the number 7

                # If the ASCII value is 84, 85 or 86
                elif ascii_value >= 84 and ascii_value <= 86:
                    print('8', end='')  # Print the number 8

                # If the ASCII value is 87, 88, 89 or 90
                elif ascii_value >= 87 and ascii_value <= 90:
                    print('9', end='')  # Print the number 9

                # If the character is not a letter
                else:
                    print(user_text_upper[position], end="")  # Print the character


# Start the program
main()
