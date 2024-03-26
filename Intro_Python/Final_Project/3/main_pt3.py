# Author: Ana Victoria Gomes Mantovani
# Date: 06/27/2023
# Final Project - main pt3

# Import the database 
import databaseio

print(" ------------------------------------ ")
print("Welcome to the database of books!")
print(" ------------------------------------ ")
print()

# Loop back to the menu until user selects '4. Exit'
while True:
    
    # Display the options menu and get user input
    user_choice = databaseio.display_menu()
    print()
    print("User choice:", user_choice)
    print()
        
    # Read and input user data
    if user_choice == 1:
        # Read input data from the user
        title, genre1, genre2, pages = databaseio.read_data()

        # Print the three attributes obtained
        databaseio.print_data(title, genre1, genre2, pages)
        
        print()
        print()
    
    # Not implemented yet
    elif user_choice == 2:    
        break
        
    # Not implemented yet
    elif user_choice == 3:  
        break
        
    # Exit the program
    else:
        print()
        print(" ------------------------------------ ")
        print("Thank you for using the database.")
        print(" ------------------------------------ ")
        break
    
