# Author: Ana Victoria Gomes Mantovani
# Date: 09/22/2023
# Program: Course Info Lookup

import re

# Add courses and description to the dictionary
course_catalog = {
    "CIS-1300": "Web Design Software - Creation of Web sites using Web design software such as DreamWeaver or FrontPage.",
    "CIS-1400": "Programming Logic and Technique - An introduction to computer-based problem-solving techniques.",
    "CIS-2211": "2D Game Scripting - Introduction to 2D game development using a scripting language.",
    "CIS-2332": "Game Animation - Course covers animating for gameplay and in-game cutscenes.",
    "CIS-2532": "Introduction to Programming with Python - Introduces the object-oriented programming language of Python.",
    "CIS-2571": "Introduction to Java - Introduction to object-based problem solving in the Java language."
}

# Create a regular expression pattern for the course ID
course_id_pattern = r'^[A-Za-z]{3}[- ]?\d{4}$'

# Function to validate the course ID format
def validate_course_id(course_id):
    return re.match(course_id_pattern, course_id)

# Function to look up the course description
def lookup_course_description(course_id):
    
    # Remove any hyphens or spaces from the course ID and convert to uppercase
    cleaned_course_id = re.sub(r'[- ]', '', course_id).upper()
    
    # Check if the cleaned course ID matches any catalog key
    for catalog_id in course_catalog:
        if cleaned_course_id == re.sub(r'[- ]', '', catalog_id).upper():
            return course_catalog[catalog_id]
    
    return None  # Return None if the course ID is not found in the catalog

# Function to display the list of course codes
def display_course_list():
    print()
    print("List of Course Codes:")
    for course_id in course_catalog:
        print(course_id)
    print()

# Main program
def main():
    while True:
        
        # Display menu
        print("Course Info Lookup Menu:")
        print("1. View List of Course Codes")
        print("2. Enter Course ID for Description")
        print("3. Exit")
        print()
        
        user_choice = input("Please select an option (1, 2, or 3): ").strip()
        
        if user_choice == '1':
            display_course_list()
        elif user_choice == '2':
            while True:  # Keep asking for the course ID until it's valid
                print()
                user_input = input("Enter a course number (e.g., CIS-2532, CIS 2532, CIS2532): ").strip()

                # Display course details if its on the dictionary
                if validate_course_id(user_input):
                    course_description = lookup_course_description(user_input)
                    if course_description:
                        print()
                        print(f"Course Details:")
                        print(f"Course ID: {user_input}")
                        print(f"Description: {course_description}")
                        print()
                    else:
                        print()
                        print(f"Course {user_input} not found in the catalog.")
                        print()
                        # Go back to the menu if there are no matching course ID
                    break  
                else:
                    print()
                    print("Invalid course ID format. Please use the format 'XXX-9999', 'XXX 9999', or 'XXX9999'.")
                    print()
                    
        # Exit the program
        elif user_choice == '3':
            print()
            print("Thank you for using the Course Info Lookup.")
            break
        
        else:
            print()
            print("Invalid choice. Please select a valid option (1, 2, or 3).")
            print()

# Start the program
if __name__ == "__main__":
    main()