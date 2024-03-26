# Author: Ana Victoria Gomes Mantovani
# Date: 10/17/2023
# Program: Data Storage and Retrieval

# Define a Contact class to store contact information
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Define a ContactBook class to manage contacts
class ContactBook:
    def __init__(self):
        # Initialize an empty list to store contacts
        self.contacts = []

    # Method to add a new contact to the contact book
    def add_contact(self, name, email, phone):
        contact = Contact(name, email, phone)
        self.contacts.append(contact)

    # Method to delete a contact by name from the contact book
    def delete_contact(self, name):
        name = name.lower()
        deleted_contacts = []

        # Iterate through contacts and remove the contact with the specified name
        for contact in self.contacts:
            if contact.name.lower() == name:
                self.contacts.remove(contact)
                deleted_contacts.append(contact)

        # Print deleted contacts
        if deleted_contacts:
            print("Deleted contacts:")
            for contact in deleted_contacts:
                print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print(f"No contact with the name '{name}' found in the contact book.")

    # Method to display contacts in ascending or descending order
    def display_contacts(self, ascending=True):
        # Sort contacts by name, either in ascending or descending order
        sorted_contacts = sorted(self.contacts, key=lambda x: x.name, reverse=not ascending)
        for contact in sorted_contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

    # Method to search contacts by name and/or email
    def search_contact(self, name=None, email=None):
        found_contacts = []
        # Iterate through contacts and check for matches based on name and/or email
        for contact in self.contacts:
            if (name is None or name.lower() in contact.name.lower()) and (email is None or email.lower() in contact.email.lower()):
                found_contacts.append(contact)
        # Print search results
        if found_contacts:
            print("Search results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

# Program
def main():
    contact_book = ContactBook()

    # Main program loop
    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Delete a contact")
        print("3. Display contacts (ascending order)")
        print("4. Display contacts (descending order)")
        print("5. Search contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # User input processing and function calls based on user choice
        if choice == '1':
            # Get contact details from user and add the contact to the contact book
            name = input("Enter the contact's name: ")
            email = input("Enter the contact's email: ")
            phone = input("Enter the contact's phone number: ")
            print("New contact added.")
            contact_book.add_contact(name, email, phone)
        elif choice == '2':
            # Get the name of the contact to delete and remove it from the contact book
            name = input("Enter the contact's name to delete: ")
            print("Contact deleted.")
            contact_book.delete_contact(name)
        elif choice == '3':
            # Display contacts in ascending order
            contact_book.display_contacts(ascending=True)
        elif choice == '4':
            # Display contacts in descending order
            contact_book.display_contacts(ascending=False)
        elif choice == '5':
            # Get search criteria from user and search contacts
            name = input("Enter the contact's name to search (leave blank to skip): ")
            email = input("Enter the contact's email to search (leave blank to skip): ")
            contact_book.search_contact(name, email)
        elif choice == '6':
            # Exit the program
            print("Thank you for using the program.")
            break
        else:
            # Invalid input message
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()