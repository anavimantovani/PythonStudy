# Author: Ana Victoria Gomes Mantovani
# Date: 07/10/2023
# Final Project - data base io

# Create an empty list to store the book data
database = []

# Define the valid genres
valid_genres = [
            'Art', 'Biography', 'Children', 'Classic', 'Comedy', 'Comic', 'Cookbook', 'Crime', 'Fantasy',
            'Fiction', 'History', 'Horror', 'LGBTQ', 'Manga', 'Music', 'Mystery', 'Nonfiction', 'Science',
            'Thriller', 'Romance'
        ]

# Function to read and validate user input for book data
def read_data():
    while True:
        title = input("Enter the title of a book: ")
        print()

        while True:
            genre1 = input("Enter a genre of the book: ").capitalize()
            print()
            if genre1 in valid_genres:
                break
            else:
                print("Invalid genre entered. Please select from the list: " + str(valid_genres))
                print()

        while True:
            try:
                pages = int(input("Enter the number of pages in the book: "))
                print()
                if pages > 0:
                    break
                else:
                    print("Number of pages cannot be negative or zero. Please try again.")
                    print()
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                print()

        # Return the collected book data as a tuple
        return title, genre1, pages

# Function to print book data
def print_data(title, genre1, pages):
    print("Title:        " + title)
    print("Genres:       " + genre1)
    print("Num of pages: " + str(pages))
    print()

# Function to display the menu and get user input
def display_menu():
    print("Menu:")
    print(" --------------------------------------- ")
    print("1. Add a new data point to the database")
    print("2. Delete an item in the database")
    print("3. Display the current database")
    print("4. Exit")
    print(" --------------------------------------- ")
    while True:
        choice = input("Please enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
            print()