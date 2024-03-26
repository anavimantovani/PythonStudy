# Airport Simulator Project
# Main Simulation Controller

from Plane import Plane
import random

def main():
    arrival_queue = []  # List for arrival queue
    terminal_occupation = [None] * 4  # List to represent terminal occupation (4 terminals)
    departure_queue = []  # List for departure queue
    archival_system = []  # List for archived data of planes
    
    for i in range(50):  # Simulate 50 events happening today
        event = random.randint(0, 3)
        
        if event == 0:  # A plane arrives
            new_plane = Plane()
            arrival_queue.append(new_plane)
            print("Arriving:", new_plane)
            
        elif event == 1:  # A plane lands
            if None in terminal_occupation:  # Check for an available terminal
                if arrival_queue:  # Check if arrival_queue is not empty before landing
                    landed_plane = arrival_queue.pop(0)  # Dequeue from arrival queue
                    terminal_index = terminal_occupation.index(None)  # Find the first available terminal
                    terminal_occupation[terminal_index] = landed_plane  # Assign plane to terminal
                    print("Landing:", landed_plane)
                else:
                    print("No plane in arrival queue for landing")
            else:
                print("No available terminal for landing")
                
        elif event == 2:  # A plane is ready to take off
            if any(plane is not None for plane in terminal_occupation):  # Check if a plane is at a terminal
                departing_plane = terminal_occupation.pop(0)  # Dequeue from terminal
                departure_queue.append(departing_plane)  # Enqueue to departure queue
                print("Taxiing:", departing_plane)
            else:
                print("No plane available for departure")
                
        elif event == 3:  # A plane has taken off
            if departure_queue:  # Check if there's a plane in the departure queue
                departed_plane = departure_queue.pop(0)  # Dequeue from departure queue
                archival_system.append(departed_plane)  # Archive the plane
                print("Departing:", departed_plane)
            else:
                print("No plane ready for takeoff")

    # Print a report of all today's planes
    print("\n\n--------------------------------------------")
    print("Report of Today's Planes:")
    print("--------------------------------------------")
    print("\nArrivals:")
    if arrival_queue:
        max_length = max(len(str(plane)) for plane in arrival_queue)
        for i, plane in enumerate(arrival_queue, 1):
            print(f"{i}. {plane.airline.ljust(max_length + 5)} Flight {plane.flightNo}")
    else:
        print("No arrivals today.")
    
    print("\nTerminals:")
    if not any(terminal_occupation):
        print("All terminals are empty.")
    else:
        for i, plane in enumerate(terminal_occupation, 1):
            if plane is not None:
                print(f"{i}. {plane.airline.ljust(max_length + 5)} Flight {plane.flightNo}")
            else:
                print(f"{i}. Empty")
    
    print("\nDepartures:")
    if not any(departure_queue):
        print("No departures today.")
    else:
        for i, plane in enumerate(departure_queue, 1):
            print(f"{i}. {plane.airline.ljust(max_length + 5)} Flight {plane.flightNo}")
    
    print("\nArchived Data:")
    if not any(archival_system):
        print("No planes have been archived.")
    else:
        for i, plane in enumerate(archival_system, 1):
            print(f"{i}. {plane.airline.ljust(max_length + 5)} Flight {plane.flightNo}")

if __name__ == "__main__":
    main()