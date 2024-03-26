

def main():
    user_name = input('Enter your first and last name: ')

    print()
    print('Your initials:', get_initials(user_name))

# line 10 is the module header or function header
def get_initials(name):

    name = name.upper()
    first_initial = name[0]
    location_of_space = name.find(' ')
    second_initial = name[location_of_space + 1]

    return first_initial + '.' + second_initial + '.'


main()
