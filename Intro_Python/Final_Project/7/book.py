# Author: Ana Victoria Gomes Mantovani
# Date: 08/01/2023
# Final Project - book.py

import databaseio

# Book class
class Book:
    
    # Constructor for the Book class
    def __init__(self, title, genre, pages):
        self.title = title
        self.genre = genre
        self.pages = pages
    
    # Display the data from the book
    def display(self):
        databaseio.print_data(self.title, self.genre, self.pages)