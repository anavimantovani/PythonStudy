#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 03 Summer 2022
# File:       Practice_03.py
# Purpose:    Calculate the total of tickets bought
####################################################### 

PRICE_TICKETS_A = 15.25  # Name the global constant for ticket A
PRICE_TICKETS_B = 11.50  # Name the global constant for ticket B
PRICE_TICKETS_C = 9.00  # Name the global constant for ticket C

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    tickets_a = int(input('Enter number of class A tickets: '))  # Prompt user for the amount of tickets A
    tickets_b = int(input('Enter number of class B tickets: '))  # Prompt user for the amount of tickets B
    tickets_c = int(input('Enter number of class C tickets: '))  # Prompt user for the amount of tickets C

    # Display the result message to the user
    display_results(tickets_a, tickets_b, tickets_c)


# Display the result message to the user
def display_results(pass_a, pass_b, pass_c):
    result_a = PRICE_TICKETS_A * pass_a  # Calculate the total of tickes A
    result_b = PRICE_TICKETS_B * pass_b  # Calculate the total of tickes B
    result_c = PRICE_TICKETS_C * pass_c  # Calculate the total of tickes C

    total = result_a + result_b + result_c  # Calculate the sum of the total of tickets A, B and C

    # Display the total of tickets bought
    print()
    print('Total: $' + str(total))


# Start the program
main()
