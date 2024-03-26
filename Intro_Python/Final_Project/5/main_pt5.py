# Author: Ana Victoria Gomes Mantovani
# Date: 07/17/2023
# Final Project - main pt5

import databaseio
from book_database import BookDatabase
from book import Book

# Create a new instance of BookDatabase
book_database = BookDatabase()

print(" ------------------------------------ ")
print("Welcome to the database of books!")
print(" ------------------------------------ ")
print()

# Loop back to the menu until the user selects '4. Exit'
while True:
    user_choice = databaseio.display_menu()
    print()
    print("User choice:", user_choice)
    print()

    # Read and input user data, create a new Book object, and add it to the database
    if user_choice == 1:
        title, genre, pages = databaseio.read_data()
        item = Book(title, genre, pages)
        book_database.addItem(item)
        print()
        print()

    # Delete the index of the database the user selects
    elif user_choice == 2:

        # If there are no books in the database, display an error message
        if book_database.numdata == 0:
            print("There are no books in the database. Cannot delete.")
            print()

        # Prompt user to select an index to delete, or display the error message if the selected index does not exist
        else:
            while True:
                try:
                    index = int(input("Enter the index of the item to delete: "))
                    if 0 <= index < book_database.numdata:
                        book_database.deleteItem(index)
                        print("Item at index", index, "deleted.")
                        break
                    else:
                        print("Invalid index. Please enter a valid index from 0 to", book_database.numdata - 1)
                        print()
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    print()
        print()

    # Display the database
    elif user_choice == 3:

        # If there are no books in the database, display an error message
        if book_database.numdata == 0:
            print("There are no books in the database.")
            print()
            print()

        # Display the database
        else:
            print("Current database:")
            print()
            book_database.displayAll()
            print()

    # Exit the program
    else:
        print()
        print(" ------------------------------------ ")
        print("Thank you for using the database.")
        print(" ------------------------------------ ")
        break