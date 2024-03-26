

def main():

    names = ['Ava Fischer', 'Chirs Rich', 'Gordon Pike', 'Matt Hoyle', 'Rose Harrison', 'Giovanni Ricci']

    found = False
    counter = 0

    search_value = input('Enter a name to seach for in the array: ')

    print()
    print()

    while not found and counter < 6:

        if names[counter].lower().find(search_value.lower()) != -1 :
            found = True
        else:
            counter += 1

    if found:
        print('That name matches the following element:', names[counter])
    else:
        print('That name was not found in the array. ')


main()
