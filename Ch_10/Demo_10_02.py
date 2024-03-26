
FILE_NAME = 'Scores.txt'

NUMBER_OF_EXAMS = 3

def main():

    menu_choice = ''

    while menu_choice != 'X':
        print()
        print()
        print('Select an option from the menu: ')
        print()

        print('A -  Add a record')
        print('B - Display all records')
        print('X - Exit the program')
        print()

        menu_choice = input('Enter your choice: ')
        menu_choice = menu_choice.upper()

        if menu_choice == 'A':
            add_record()
        elif menu_choice == 'B':
            display_records()
        elif menu_choice != 'X':
            print()
            print('Invalid choice. Please re-enter.')
            print()


def add_record():
    print()

    output_file = open(FILE_NAME, 'a')

    student_name = input('Enter the student\'s first name: ')

    output_file.write(student_name + '\n')

    for counter in range(0, NUMBER_OF_EXAMS):
        score = int(input('Enter ' + student_name + '\'s score for exam #' + str(counter + 1) + ': '))
        output_file.write(str(score) + '\n')

    print()

    output_file.close()


def display_records():
    print()

    input_file = open(FILE_NAME, 'r')

    student_name = input_file.readline().rstrip()

    while student_name != '':
        print(format(student_name, '20s'), end='')

        for counter in range(0, NUMBER_OF_EXAMS):
            score = int(input_file.readline().rstrip())
            print(format(score, '4d'), end='')

        print()
        student_name = input_file.readline().rstrip()

    input_file.close()

    print()


main()
