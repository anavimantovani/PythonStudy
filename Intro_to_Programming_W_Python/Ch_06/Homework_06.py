#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 6 Summer 2022
# File:       Homework_06.py
# Purpose:    Calculate an avarage and grade
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    test1 = float(input('Enter test score #1: '))  # Prompt user for test score #1
    test2 = float(input('Enter test score #2: '))  # Prompt user for test score #2
    test3 = float(input('Enter test score #3: '))  # Prompt user for test score #3
    test4 = float(input('Enter test score #4: '))  # Prompt user for test score #4
    test5 = float(input('Enter test score #5: '))  # Prompt user for test score #5

    # Display the results
    print()
    print('Results:')

    print('Test #1:', determine_grade(test1))  # Display grade for the test #1
    print('Test #2:', determine_grade(test2))  # Display grade for the test #2
    print('Test #3:', determine_grade(test3))  # Display grade for the test #3
    print('Test #4:', determine_grade(test4))  # Display grade for the test #4
    print('Test #5:', determine_grade(test5))  # Display grade for the test #5
    print('-------- ----')  # Display dash to separate the grade from the average

    # Display the average of the scores
    print('Average:', format(calc_average(test1, test2, test3, test4, test5), '.1f'))


# Calculate the test grades
def determine_grade(grade):

    if grade >= 90:  # If grade is greater or equal to 90
        return 'A'  # Return the grade A
    elif grade >= 80:  # If grade is greater or equal to 80
        return 'B'  # Return the grade B
    elif grade >= 70:  # If grade is greater or equal to 70
        return 'C'  # Return the grade C
    elif grade >= 60:  # If grade is greater or equal to 60
        return 'D'  # Return the grade D
    else:  # If grade is less than 60
        return 'F'  # Return the grade F


# Calculate the average score of the tests
def calc_average(test1, test2, test3, test4, test5):

    average = (test1 + test2 + test3 + test4 + test5) / 5  # Calculate the average
    return average  # Return the average


# Start the program
main()
