
MAX_SIZE = 100

def main():
    items = [0.0] * MAX_SIZE

    number_items = 0

    value = -1

    while value != 0:

        value = float(input('Enter a positive number to add to the items (or 0 when done): '))

        # Case 1 - The list is currently empty
        if number_items == 0:
            items[0] = value
            number_items = 1

        # Case 2 - The new number is larger than all the numbers in the list
        elif value >= items[number_items - 1]:
            items[number_items] = value
            number_items += 1

        # Case 3 - The number in the middle - shift is required
        elif value != 0:

            insert_position = 0

            while items[insert_position] <= value:
                insert_position += 1

            for counter in range(number_items - 1, insert_position - 1, -1):
                items[counter + 1] = items[counter]

            items[insert_position] = value
            number_items += 1


    print()
    print()

    print('Here is the list in sorted order:')

    for counter in range(0, number_items):
        print(items[counter])


main()
