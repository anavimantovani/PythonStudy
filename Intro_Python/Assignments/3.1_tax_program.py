# Author: Ana Victoria Gomes Mantovani
# Date: 06/27/2023
# Assignment 3.1 - tax_programVer2.py

# Prompt user for item's price
price = float(input("Please enter your item's price: "))

# Calculate the tax and the total
tax = price * 0.0625
total = price + tax

# Display user's total
print()
print("Your total is:")
print(f"Subtotal:     ${price:>8.2f}")
print(f"Sales tax:    ${tax:>8.2f}")
print(f"Total:        ${total:>8.2f}")

# Prompt user for tipping
print()
tip_choice = input("Would you like to leave a tip? (y/n): ")

# Check if user enter a valid answer
while tip_choice.lower() != "y" and tip_choice.lower() != "n":
    print()
    print("Invalid answer. Please enter 'y' for yes or 'n' for no.")
    tip_choice = input("Would you like to leave a tip? (y/n): ")

# If user answers 'yes', then ask for the tip amount and display new total
if tip_choice.lower() == "y":
    print()
    tip = float(input("Enter the tip amount: $ "))
    new_total = total + tip
    print()
    print(f"Tip:          ${tip:>8.2f}")
    print(f"New total:    ${new_total:>8.2f}")
    
# If user answers 'no', display a goodbye message
else:
    print()
    print("Thank you for your purchase. Goodbye!")