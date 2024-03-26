# Author: Ana Victoria Gomes Mantovani
# Date: 07/17/2023
# Final Project - book_database.py

import databaseio
import csv
from book import Book

# Book Database class
class BookDatabase:
    
    # Constructor
    def __init__(self):
        self.database = []
        self.numdata = 0
    
    # Add new item to the database
    def addItem(self, item):
        self.database.append(item)
        self.numdata += 1
    
    # Delete an item from the database
    def deleteItem(self, index):
        if 0 <= index < len(self.database):
            self.database.pop(index)
            self.numdata -= 1
    
    # Retrieve an item from the database
    def getItem(self, index):
        if 0 <= index < len(self.database):
            return self.database[index]
    
    # Display the database
    def displayAll(self):
        for i in range(len(self.database)):
            self.getItem(i).display()
            
    # Save the database to a csv file        
    def save(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.database:
                writer.writerow([book.title, book.genre, book.pages])

    # Load the database from a csv file
    def load(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                title, genre, pages = row
                book = Book(title, genre, int(pages))
                self.addItem(book)