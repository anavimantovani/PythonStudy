# Author: Ana Victoria Gomes Mantovani
# Date: 06/27/2023
# Final Project pt 2

# Input user for the title of the book
title = input("Enter the title of a book: ")
print()

# Create a list with the valid genres of books
valid_genres = [
    'Art', 'Biography', 'Children', 'Classic', 'Comedy', 'Comic', 'Cookbook', 'Crime', 'Fantasy', 'Fiction', 'History', 'Horror', 'LGBTQ', 'Manga', 'Music', 'Mystery', 'Nonfiction', 'Science', 'Thriller', 'Romance'
    ]

# Check if user input is on the valid genre
while True:
    genre1 = input("Enter a genre of the book: ").capitalize()
    if genre1 in valid_genres:
        break
    else:
        print("Invalid genre entered. Please select from the list: " + str(valid_genres))
        print()
print()

# Check if user input is on the valid genre
while True:
    genre2 = input("Enter a second genre of the book: ").capitalize()
    if genre2 in valid_genres:
        break
    else:
        print("Invalid genre entered. Please select from the list: " + str(valid_genres))
        print()
print()

# Check if user input is a positive integer
while True:
    try:
        pages = int(input("Enter the number of pages in the book: "))
        if pages > 0:
            break
        else:
            print("Number of pages cannot be negative or zero. Please try again.")
            print()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        print()

# Display the data of the book
print()
print("Book:")
print("Title: " + title)
print("Genres: " + genre1 + " and " + genre2)
print("Num of pages: " + str(pages))