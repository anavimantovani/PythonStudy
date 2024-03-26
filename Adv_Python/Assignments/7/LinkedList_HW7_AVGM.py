# Author: Ana Victoria Gomes Mantovani
# Date: 10/25/2023
# Program: No duplicates linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __del__(self):
        print(self.data, "was removed")


class LinkedList:
    def __init__(self):
        self.__first = Node(None)

    def isEmpty(self):
        return self.__first.next is None

    def display(self):
        temp = self.__first.next
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def addFront(self, value):
        newNode = Node(value)
        newNode.next = self.__first.next
        self.__first.next = newNode

    def addBack(self, value):
        temp = self.__first
        while temp.next is not None:
            temp = temp.next

        # Check for duplicates before adding
        if not self.contains(value):
            temp.next = Node(value)

    def removeFront(self):
        temp = self.__first.next
        self.__first.next = temp.next
        temp.next = None

    def removeBack(self):
        temp = self.__first.next
        trailer = self.__first

        while temp.next is not None:
            temp = temp.next
            trailer = trailer.next

        trailer.next = None

    def search(self, key):
        temp = self.__first.next
        while temp is not None:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def remove(self, value):
        trailer = self.__first
        temp = trailer.next

        while temp is not None and temp.data != value:
            temp = temp.next
            trailer = trailer.next

        if temp is not None:
            trailer.next = temp.next
            temp.next = None

    def count(self):
        counter = 0
        temp = self.__first.next
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter

    def contains(self, value):
        temp = self.__first.next
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False


################
# Test Program #
################
linkedList = LinkedList()

print("List contains", linkedList.count(), "nodes")

if linkedList.isEmpty():
    print("Empty")
else:
    print("Contains data")

for i in range(10):
    linkedList.addFront(i * 2)
    linkedList.addBack(i * 10)

# Add duplicate values, which will be prevented
linkedList.addBack(20)
linkedList.addFront(18)

print("List contains", linkedList.count(), "nodes")

if linkedList.isEmpty():
    print("Empty")
else:
    print("Contains data")

linkedList.display()

linkedList.removeFront()
linkedList.display()

linkedList.removeBack()
linkedList.display()

print("List contains", linkedList.count(), "nodes")

while True:
    print()
    key = int(input("Enter search key (-1 to quit): "))
    if key == -1:
        break
    if linkedList.search(key) is None:
        print("Nope, didn't find", key)
        print()
    else:
        print("Yep, found", key)
        print()

while True:
    print()
    key = int(input("Enter value to remove (-1 to quit): "))
    if key == -1:
        break
    linkedList.remove(key)
    linkedList.display()

print("List contains", linkedList.count(), "nodes")