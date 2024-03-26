#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 8 Summer 2022
# File:       Homework_08.py
# Purpose:    Exam grader
####################################################### 

QUESTIONS_ANSWERS_USER = 20  # Total of questions on the test
# Correct answers on the test
CORRECT_ANSWERS = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    user_answers = [''] * QUESTIONS_ANSWERS_USER  # Create an array to store the answers

    # Get the user's answers
    for counter in range(0, QUESTIONS_ANSWERS_USER):
        # Prompt user for their answers
        user_answers[counter] = input('What is the answer for question ' + format(counter + 1, '2') + ': ')

    answers = CORRECT_ANSWERS  # Set an array for the correct answers
    correct_answer = 0  # Set variable to 0 so loop can start
    wrong_answer = 0  # Set variable to 0 so loop can start
    counter = 0  # Set variable to 0 so loop can start
    display_wrong_answers = [0] * QUESTIONS_ANSWERS_USER  # Set array to keep the wrong answers

    # While the counter is less than the total answers
    while counter < QUESTIONS_ANSWERS_USER:

        # If the user's answers is correct
        if user_answers[counter].lower() == answers[counter].lower():
            correct_answer += 1  # Add 1 answer to the correct pool

        # If the user's answer is incorrect
        else:
            wrong_answer += 1  # Add 1 answer to the incorrect pool
            display_wrong_answers[counter] += 1  # Store which answer was wrong

        counter += 1  # Add 1 to the counter so the loop keeps iterating

    print()  # Print a blank line

    #  If there are 15+ correct answers
    if correct_answer >= 15:
        print('*** PASSED ***')  # Tell user that they passed

    # If there are less than 15 correct answers
    else:
        print('*** NOT PASSED ***')  # Tell the user they did not pass

    print(format('Number correct:', '18s'), correct_answer)  # Display the total of correct answers
    print(format('Number incorrect:', '18s'), wrong_answer)  # Display the total of incorrect answers

    # If user got one or more questions wrong
    if wrong_answer > 0:

        # Display the user a message to show the questions he got wrong
        print()
        print()
        print('You got the following questions wrong:')

        # Display a header to the table to show the question, correct answer and user's answer
        print()
        print('Question  Correct  Your Answer')
        print('--------  -------  -----------')

        # Display the question number, the correct answer and the user's answer
        for result_counter in range(0, QUESTIONS_ANSWERS_USER):

            # If there are elements on the array of wrong questions
            if display_wrong_answers[result_counter] != 0:
                print(format(result_counter + 1, '4'), end='')  # Display the question number
                print('        ', format(answers[result_counter], '11'), end='')  # Display the correct answer
                print(user_answers[result_counter].upper())  # Display the user's answer

    # If there are no elements on the wrong answer's array
    else:
        print()  # Print a blank line


# Start the program
main()
