#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Practice 6 Summer 2022
# File:       Practice_06.py
# Purpose:    Calculate the Kinetic Energy
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    # Prompt user for the mass of the object
    object_mass = float(input('Enter the mass of the object in kilograms: '))

    # Prompt user for the valocity of the object
    object_velocity = float(input('Enter the velocity of the object in meters per second: '))

    # Display the result in Joules to the user
    print()
    print('Joules:', calculate_kinetic_energy(object_mass, object_velocity))


# Calculate the kinetic energy of the entered values
def calculate_kinetic_energy(mass, velocity):

    result_ke = 0.5 * mass * velocity ** 2  # Calculate the total kinetic energy

    return result_ke  # Return the result to the main module


# Start the program
main()
