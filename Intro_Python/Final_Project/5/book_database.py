# Author: Ana Victoria Gomes Mantovani
# Date: 07/17/2023
# Final Project - book_database.py

import databaseio

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