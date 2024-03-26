######
#
######

# Strat of program
def main():
    user_name = input('Enter your first name: ')  # Prompt user for name
    user_age = int(input('Enter your age: '))  # Prompt user for age

    # Display the result message to the user
    display_results(user_name, user_age)


# Display the result message to the user
def display_results(name, age):
    # Display the user's name and current age
    print('Your name is', name, 'and your age is', age)

    # Display the user's age in ten years
    print('In 10 years you will be', age + 10, 'years old.')


main()  # Start of the program
