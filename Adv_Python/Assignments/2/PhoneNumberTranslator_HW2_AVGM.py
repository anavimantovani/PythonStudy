# Author: Ana Victoria Gomes Mantovani
# Date: 09/08/2023
# Program: Phone Number Translator

# Main function to run the program
def main():
    
    # Dictionary containing the letter to number equivalent
    letter_to_digit = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7', 
        't': '8', 'u': '8', 'v': '8', 
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    
    # Greeting message
    print("------------------------------------------------")
    print("Welcome to the Phone Number Translator program!")
    print("------------------------------------------------")
    print()

    while True:
        # Prompt user for the string or if they want to exit the program
        user_input = input("Enter a telephone number in letters or digits (or -1 to quit): ")

        # Check if the user wants to quit
        if user_input == "-1":
            print("---------------------------------------------------------")
            print("Thank you for using the Phone Number Translator program!")
            print("---------------------------------------------------------")
            print()
            break

        # Remove spaces and convert input to lowercase
        user_input = user_input.replace(' ', '').lower()
        user_input = user_input.replace('-', '')

        # Process only the first seven characters
        user_input = user_input[:7]

        # Create list for the translated phone number
        result = []

        # Translate letter to number or append the existing number
        for char in user_input:
            if char.isalpha():
                result.append(letter_to_digit.get(char, ''))
            elif char.isdigit():
                result.append(char)

        # Insert hyphen after the third digit
        result.insert(3, '-')

        # Convert the result list to a string
        phone_number = ''.join(result)

        # Display the converted string
        print("Telephone number translated to digits:", phone_number)
        print()

# Start program
if __name__ == "__main__":
    main()