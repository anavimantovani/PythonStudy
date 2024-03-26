#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 8 Summer 2022
# File:       Practice_08.py
# Purpose:    Lottery number generator
####################################################### 

import random  # Import random numbers

NUM_OF_MACHINES = 7  # Number of lotto machines
NUM_OF_BALLS = 10  # Number of balls in each machine

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    machines = [0] * NUM_OF_MACHINES  # Create an array to store the numbers

    # Pick the wining numbers
    for counter in range(0, NUM_OF_MACHINES):
        machines[counter] = random.randint(0, NUM_OF_BALLS - 1)  # Generate the random number

    print('The winning lottery numbers are: ', end='')  # Display the result message

    # Display the winning numbers
    for counter in range(0, NUM_OF_MACHINES):
        print(machines[counter], '', end='')  # Display the winning numbers

    print()  # Print a blank line


# Start the program
main()
