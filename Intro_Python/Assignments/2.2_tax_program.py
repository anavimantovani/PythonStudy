# Author: Ana Victoria Gomes Mantovani
# Date: 06/20/2023
# Assignment 2.2 - tax_program.py

price = float(input("Please enter your item's price: "))

tax = price * 0.0625
total = price + tax

print()
print("Your total is:")
print(f"Subtotal:     ${price:>4.2f}")
print(f"Sales tax:    ${tax:>04.2f}")
print(f"Total:        ${total:>4.2f}")