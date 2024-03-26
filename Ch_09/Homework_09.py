#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 9 Summer 2022
# File:       Homework_09.py
# Purpose:    Sort and name lookup
####################################################### 

NAMES_ENTERED = 20  # Array size

# Start the program
def main():
    print('\n  Ana Victoria Gomes Mantovani  \n')  # Display author's name

    enter_names = [''] * NAMES_ENTERED  # Define the array

    print('Please enter 20 names:')  # Header to ask the user for 20 names

    # Prompt user for 20 names
    for counter in range(0, NAMES_ENTERED):
        enter_names[counter] = input(format(counter + 1) + ': ')  # Ask user for the 20 names

    # Header to display the names sorted in ascending order
    print()
    print('The names sorted are:')

    sorted_names = bubble_sort(enter_names)  # Define the bubble sort

    # Display the names sorted
    for print_counter in range(0, NAMES_ENTERED):
        print(sorted_names[print_counter])  # Display the names sorted

    search_name = 'aa'  # Set variable so loop can start

    while search_name != '':
        # Prompt user for the name they want to lookup
        print()
        search_name = input('Enter a name to search for (or Enter to exit): ')

        # If the input is not equal to Enter
        if search_name != '':

            print()  # Print a blank line

            response = binary_search(sorted_names, search_name)  # Define the binary search

            # If the array position is not equal to -1
            if response[0] != -1:
                print('Name Found:', search_name)  # Display the name
                print('Position:', response[0])  # Display the position
                print('Array Lookups:', response[1])  # Display the amount of lookups

            # If the name cannot be found
            else:
                print('Name not found.')  # Tell the user the name was not found
                print('Array Lookups', response[1])  # Display the amount of lookups


# Sort names with the bubble sort
def bubble_sort(array):

    # For loop so the loop keeps interating
    for counter in range(0, len(array) - 1):

        # For loop so the array can be sorted
        for counter_bubble in range(0, len(array) - 1):

            # If the number in the higher position is bigger than the number before
            if array[counter_bubble] > array[counter_bubble+1]:
                temp = array[counter_bubble]  # Set temporary varibale to store the number
                array[counter_bubble] = array[counter_bubble+1]  # Change variables places
                array[counter_bubble+1] = temp  # Replace the variable number with the temporary variable

    return array  # Return the array


# Lookup the array for the given name
def binary_search(array_names, name_target):
    low = 0  # Set the lowest position in the array
    high = len(array_names) - 1  # Set the highest position in the array
    counter_lookup = 0  # Set variable so the loop can start

    # While the highes position is bigger or equal to the lowest
    while low <= high:
        mid = low + (high - low) // 2  # Calculate the mid point and round it down

        # If the name is not found in the array
        if array_names[mid] == name_target:
            counter_lookup += 1  # Add 1 to the lookup counter
            return [mid, counter_lookup]  # Return the mid point and the amount of lookups

        # If the target name is bigger than the mid point
        elif array_names[mid] < name_target:
            low = mid + 1  # Set lowest point as the mid point plus 1 position
            counter_lookup += 1  # Add 1 to the lookup counter

        # If the target is smaller than the mid point
        else:
            high = mid - 1  # Set the highest point as the mid point minus 1
            counter_lookup += 1  # Add 1 to the lookup counter

    return [-1, counter_lookup]  # Return the position -1 and the amount of lookups


# Start the program
main()
