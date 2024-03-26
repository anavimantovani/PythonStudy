# Author: Ana Victoria Gomes Mantovani
# Date: 08/31/2023
# Program: Fahrenheit and Celcius conversion program

# Function to convert fahrenheit to celcius
def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Function to convert celcius to fahrenheit
def cels_to_fahr(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to display the temperature conversion table
def conversion_table():
    
    # Heading of the table
    print("+" + "---------------" + "+" + "---------------" + "+")
    print("|{:^15}|{:^15}|".format("Fahrenheit", "Celsius"))
    print("+" + "---------------" + "+" + "---------------" + "+")
    
    # For loop to calculate and display the table content
    for fahrenheit in range(0, 101, 10):
        celsius = fahr_to_cels(fahrenheit)
        print("|{:^15.2f}|{:^15.2f}|".format(fahrenheit, celsius))
    print("+" + "---------------" + "+" + "---------------" + "+")

# Main function to display the program
def main():
    
    # Program header
    print("------------------------------------------------------ ")
    print("Welcome to the Fahrenheit-Celcius conversion program!")
    print("------------------------------------------------------ ")
    
    # Keep the program working unless the user selects option 4
    while True:
        
        # Display menu
        print()
        print("---------------------------------------------")
        print("Temperature Conversion Menu:")
        print("---------------------------------------------")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Display a temperature conversion table")
        print("4. Exit program")
        print("---------------------------------------------")
        print()

        choice = input("Enter your choice (1-4): ")

        # Convert user input to Celcius
        if choice == '1':
            print()
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            print()
            celsius = fahr_to_cels(fahrenheit)
            print(f"{fahrenheit:.2f}° Fahrenheit is equal to {celsius:.2f}° Celsius.")
            print()

        # Convert user input to Fahrenheit
        elif choice == '2':
            print()
            celsius = float(input("Enter the temperature in Celsius: "))
            print()
            fahrenheit = cels_to_fahr(celsius)
            print(f"{celsius:.2f}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit.")
            print()

        # Display the conversion table
        elif choice == '3':
            print()
            conversion_table()
            print()

        # Exit the program
        elif choice == '4':
            print()
            print("---------------------------------")
            print("Thank you for using the program!")
            print("---------------------------------")
            print()
            break

        # Display error if user input is not one of the menu options 
        else:
            print()
            print("Invalid choice. Please choose a valid option ( 1 / 2 / 3 / 4 ).")
            print()

# Start program
if __name__ == "__main__":
    main()
