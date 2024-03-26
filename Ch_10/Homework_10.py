#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 10 Summer 2022
# File:       Homework_10.py
# Purpose:    Game Information list
####################################################### 

FILE_NAME = 'output.csv'  # Name the file

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    output_file = open(FILE_NAME, 'w')  # Open the file
    # Write the header on the file
    output_file.write('Game' + ',' + 'Company name' + ',' + 'Active players' + ',' + 'Rating' + '\n')

    menu_choice = ''  # Set variable so loop can start

    # While the menu choice is not 'n'
    while menu_choice != 'n':

        name_of_game = enter_game_name()  # Prompt user for the name of the game
        company_name = enter_company_name()  # Prompt user for the name of the company
        player = enter_active_players()  # Prompt user for the number of active players
        rating = enter_game_rating()  # Prompt user for the rating of the game

        # Write the answers of the user in the file
        output_file.write(name_of_game + ',' + company_name + ',' + str(player) + ',' + str(rating) + '\n')

        # Ask the user if they want to keep going or stop the program.
        print()
        menu_choice = input('Do you want to add more(y/n)? ')
        menu_choice = menu_choice.lower()
        print()

    output_file.close()  # Close the file


# Prompt user for the name of the game
def enter_game_name():

    # Ask user for the name of the game
    name = input('Please enter the game name: ')

    return name  # Return the name of the game


# Prompt user for the name of the company
def enter_company_name():

    # Ask user for the name of the company
    company = input('Please enter the game\'s company name: ')

    return company  # Return the name of the company


# Prompt user for the number of active players
def enter_active_players():

    # Ask user for the number of players
    player = int(input('Plase enter the number of active players: '))

    return player  # Return the number of active players


# Prompt user for the rating of the game
def enter_game_rating():

    # Ask user for the rating of the game
    rating = int(input('Please enter your rating for the game(0-5, no decimals): '))

    return rating  # Return the rating of the game


# Start the program
main()
