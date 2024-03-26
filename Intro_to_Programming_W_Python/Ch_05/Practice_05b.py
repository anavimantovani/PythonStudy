#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 5b Summer 2022
# File:       Practice_05b.py
# Purpose:    Turtle Spiral Curve
####################################################### 

import turtle  # import turtle

print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

side = 50  # Declare the variable so the loop can start

# Perform the loop 37 squares, each time make the square 5 pixels bigger than the
# last one and turn it 10 degrees to the right
for square in range(1, 38):

    # Perform the loop to make a square
    for first_square in range(1, 5):
        turtle.forward(side)  # Make the turtle move forward
        turtle.right(90)  # Rotate the turtle to the right in 90 degrees

    turtle.right(10)  # Rotate the turtle to the right in 10 degrees
    side = side + 5  # Increase the side of the square in 5 pixels


