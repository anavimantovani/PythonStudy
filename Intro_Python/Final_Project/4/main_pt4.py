# Author: Ana Victoria Gomes Mantovani
# Date: 07/10/2023
# Final Project - main pt4

# Import the database 
import databaseio

# Create an empty list to store the book data
database = []

print(" ------------------------------------ ")
print("Welcome to the database of books!")
print(" ------------------------------------ ")
print()

# Loop back to the menu until user selects '4. Exit'
while True:
    user_choice = databaseio.display_menu()
    print()
    print("User choice:", user_choice)
    print()

    # Read and input user data
    if user_choice == 1:
        title, genre1, pages = databaseio.read_data()
        database.append((title, genre1, pages))
        print()
        print()

    # Delete the index of the database the user selects
    elif user_choice == 2:
        
        # If there are no boons in the database, display an error message
        if len(database) == 0:
            print("There are no books in the database. Cannot delete.")
            print()
            
        # Prompt user to select an index to delete, or display the error message if the selected index does not exist
        else:
            while True:
                try:
                    index = int(input("Enter the index of the item to delete: "))
                    if 0 <= index < len(database):
                        database.pop(index)
                        print("Item at index", index, "deleted.")
                        break
                    else:
                        print("Invalid index. Please enter a valid index from 0 to", len(database) - 1)
                        print()
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    print()
        print()

    # Display the database
    elif user_choice == 3:
        
        # If there are no books in the database, display an error message
        if len(database) == 0:
            print("There are no books in the database.")
            print()
            print()
        
        # Display the database
        else:
            print("Current database:")
            print()
            for index, item in enumerate(database):
                title, genre1, pages = item
                print("Book index:  ", index)
                databaseio.print_data(title, genre1, pages)
            print()

    # Exit the program
    else:
        print()
        print(" ------------------------------------ ")
        print("Thank you for using the database.")
        print(" ------------------------------------ ")
        break