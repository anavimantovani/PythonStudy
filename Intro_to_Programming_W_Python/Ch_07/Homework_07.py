#######################################################
# Name:       Ana Victoria Gomes Mantovani
# Class:      CIS-1400
# Assignment: Homework 7 Summer 2022
# File:       Homework_07.py
# Purpose:    Speeding Violations calculator
####################################################### 

# Start the program
def main():
    print('\n**  Ana Victoria Gomes Mantovani  **\n')  # Display author's name

    speed_limit = ask_speed_limit()  # Prompt user for the speed limit
    car_speed = ask_car_speed(speed_limit)  # Prompt user fot the vehicle speed
    fine_calc(speed_limit, car_speed)  # Calculate the fine and display results


# Ask user for the speed limit
def ask_speed_limit():

    # Ask user for the speed limit
    speed_lim = int(input('Please enter the speed limit: '))

    # The speed limit must be between 20 and 70
    while speed_lim < 20 or speed_lim > 70:

        # Display an ERROR message to the user
        print()
        print('ERROR: Speed limit must be between 20 and 70')
        print()

        # Ask user for the speed limit again
        speed_lim = int(input('Please enter the speed limit: '))

    return speed_lim  # Return the speed limit


# Ask user for the vehicle speed
def ask_car_speed(limit):

    speed_limit_error = limit + 1  # Speed of vehicle must be more than the speed limit

    # Ask user for the vechicle speed
    print()
    print()
    vehicle_speed = int(input('Please enter vehicle speed: '))

    # The vehicle speed must be more than the speed limit and less than 200
    while vehicle_speed < speed_limit_error or vehicle_speed >= 200:

        # Display an ERROR message to the user
        print()
        print('ERROR: Vehicle speed must be between', speed_limit_error, 'and 199')
        print()

        # Ask user for the vechicle speed again
        vehicle_speed = int(input('Please enter vehicle speed: '))

    return vehicle_speed  # Return the vehicle speed


# Calculate the fine
def fine_calc(limit_road, vehicle):
    exceeded = vehicle - limit_road  # Calculate the exceeded speed
    fine = 0  # Set variable to zero so the conditional statement can start

    print()  # Print a blank line

    # If the vehicle exceeded the limit by 21+ MPH
    if exceeded >= 21:

        fine = 300  # Set fine to 300
        # Display the results
        print('Exceeded speed limit by 21+ MPH. ' + '$' + str(fine) + ' fine.')

    # If the vehicle exceeded the limit by 16-20 MPH
    elif exceeded >= 16:

        fine = 150  # Set fine to 150
        # Display the results
        print('Exceeded speed limit by 16-20 MPH. ' + '$' + str(fine) + ' fine.')

    # If the vehicle exceeded the limit by 11-15 MPH
    elif exceeded >= 11:

        fine = 75  # Set fine to 75
        # Display the results
        print('Exceeded speed limit by 11-15 MPH. ' + '$' + str(fine) + ' fine.')

    # If the vehicle exceeded the limit by 1-10 MPH
    else:

        fine = 50  # Set fine to 50
        # Display the results
        print('Exceeded speed limit by 1-10 MPH. ' + '$' + str(fine) + ' fine.')


# Start the program
main()
