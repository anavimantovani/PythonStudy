# Author: Ana Victoria Gomes Mantovani
# Date: 06/27/2023
# Assignment 3.2 - 3.2_bottles_song.py

# Prompt user for a number of bottles
num_bottles = int(input("How many bottles? Please enter an integer: "))
print()

# Check if num_bottles is a positive integer
while num_bottles <= 0:
    print("Invalid input. Please enter a positive integer.")
    num_bottles = int(input("How many bottles? Please enter a positive integer: "))
    print()

# Go over the loop, subctracting one bottle every iteration and altering the output
for num in range(num_bottles, 0, -1):
    
    if num == 1:
        bottle_plural = "bottle"
        bottles_left = "no more bottles"
    elif num == 2:
        bottle_plural = "bottles"
        bottles_left = "1 bottle"
    else:
        bottle_plural = "bottles"
        bottles_left = str(num - 1) + " bottles"

    print(f"{num} {bottle_plural} of water on the wall, {num} {bottle_plural} of water!")
    print(f"Take one down, pass it around, {bottles_left} of water!")
    print()

print("Done!")