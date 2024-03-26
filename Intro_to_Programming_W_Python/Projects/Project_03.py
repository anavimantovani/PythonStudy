#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Project_03 Summer 2022
# File:       Project_03.py
# Purpose:    Rock Papers Scissors Game
####################################################### 

import random  # Import the random function

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    user_selection = ''  # Set variable so loop can start
    user_win_counter = 0  # Set counter to 0
    user_lose_counter = 0  # Set counter to 0
    tie_counter = 0  # Set counter to 0

    # While use didn't select X
    while user_selection != 'X':

        user_selection = get_user_selection()  # Get user selection
        computer_selection = get_computer_selection()  # Get computer selection

        # If user didn't select X
        if user_selection != 'X':

            # If user selects rock and computer selects rock
            if user_selection == 'R' and computer_selection == 'R':

                tie_counter += 1  # Add 1 to the tie counter

                # Display a tie message to the user
                print()
                print('Computer picked rock. Tie.')

            # If user selects rock and computer selects paper
            elif user_selection == 'R' and computer_selection == 'P':

                user_lose_counter += 1   # Add 1 to the lose counter

                # Display a lose message to the user
                print()
                print('Computer picked paper. Paper covers rock. You lose...')

            # If user selects rock and computer selects scissors
            elif user_selection == 'R' and computer_selection == 'S':

                user_win_counter += 1  # Add 1 to the win counter

                # Display a win message to the user
                print()
                print('Computer picked scissors. Rock blunts scissors. You win!!!')

            # If user selects paper and computer selects rock
            elif user_selection == 'P' and computer_selection == 'R':

                user_win_counter += 1  # Add 1 to the win counter

                # Display a win message to the user
                print()
                print('Computer picked rock. Paper covers rock. You win!!!')

            # If user selects paper and computer selects paper
            elif user_selection == 'P' and computer_selection == 'P':

                tie_counter += 1  # Add 1 to the tie counter

                # Display a tie message to the user
                print()
                print('Computer picked paper. Tie.')

            # If user selects paper and computer selects scissors
            elif user_selection == 'P' and computer_selection == 'S':

                user_lose_counter += 1   # Add 1 to the lose counter

                # Display a lose message to the user
                print()
                print('Computer picked scissors. Scissors cut paper. You lose...')

            # If user selects scissors and computer selects rock
            elif user_selection == 'S' and computer_selection == 'R':

                user_lose_counter += 1   # Add 1 to the lose counter

                # Display a lose message to the user
                print()
                print('Computer picked rock. Rock blunts scissors. You lose...')

            # If user selects scissors and computer selects paper
            elif user_selection == 'S' and computer_selection == 'P':

                user_win_counter += 1  # Add 1 to the win counter

                # Display a win message to the user
                print()
                print('Computer picked paper. Scissors cut paper. You win!!!')

            # If user selects scissors and computer selects scissors
            elif user_selection == 'S' and computer_selection == 'S':

                tie_counter += 1  # Add 1 to the tie counter

                # Display a tie message to the user
                print()
                print('Computer picked scissors. Tie.')

        # If user selects X
        else:
            print()  # Display a blank line
            print('RESULTS:')  # Display the results header

            # Display how many times the user won
            print('     You won ' + str(user_win_counter) + ' time(s).')

            # Display how many times the user lost
            print('     The computer won ' + str(user_lose_counter) + ' time(s).')

            # Display how many times there was a tie
            print('     There were ' + str(tie_counter) + ' tie(s).')


# Get the user selection
def get_user_selection():

    print()  # Display a blank line

    # Prompt user for his selection
    user_choice = input('Choose (r)ock, (p)aper, (s)cissors, or e(x)it: ')

    user_choice = user_choice.upper()  # Change the selection to uppercase

    # While the user doesn't enter R, P, S or X
    while user_choice != 'R' and user_choice != 'P' and user_choice != 'S' and user_choice != 'X':

        user_choice = input('Invalid choice. Please try again: ')  # Prompt user again
        user_choice = user_choice.upper()  # Change the selection to uppercase

    return user_choice  # Return the user's selection


# Get the computer selection
def get_computer_selection():

    computer_random = random.randint(1, 3)  # Computer picks a random number from 1 to 3

    # If the computer picks the number 1
    if computer_random == 1:

        computer_choice = 'R'  # Set the computer choice as rock

    # If the computer picks the number 2
    elif computer_random == 2:

        computer_choice = 'P'  # Set the computer choice as paper

    # If the computer picks the number 3
    elif computer_random == 3:

        computer_choice = 'S'  # Set the computer choice as scissors

    return computer_choice  # Return the computer's choice


# Start the program
main()
