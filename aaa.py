#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 10 Summer 2022
# File:       Homework_10.py
# Purpose:    Game information List
#######################################################

FILE_NAME = 'output.csv'

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    output_file = open(FILE_NAME, 'w')
    output_file.write('Game' + ',' + 'Company name' + ',' + 'Active players' + ',' + 'Rating' + '\n')
    output_file.close()

    info = enter_game_info()

    menu_choice = ''

    while menu_choice != 'n':
        print()
        menu_choice = input('Do you want to add more(y/n)? ')
        menu_choice = menu_choice.lower()

        if menu_choice == 'y':
            print()
            enter_game_info()

        elif menu_choice != 'n':
            print()
            print('Invalid answer. Please re-enter.')
            print()


def enter_game_info():

    name = input('Please enter the game name: ')
    company = input('Please enter the game\'s company name: ')
    player = int(input('Plase enter the number of active players: '))
    rating = int(input('Please enter your rating for the game(1-10): '))

    output_file = open(FILE_NAME, 'w')
    output_file.write(name + ',' + company + ',' + str(player) + ',' + str(rating))
    output_file.close()


main()
