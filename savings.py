### Savings Program Made By Dom @ 2022 ###

import sys
import time

print("Welcome to the Python Saving Program!")
start = input("Would you liken to start? (Respond with yes to start) ")

if start != "yes":
    quit()

print("Ok let's begin")

balance=int(input("Enter your savings balance (no $ sign): "))

time.sleep(3)

print("--")
print("--")
print("--")
print("--")
print("--")
print("--")
print("--")
print("--")
print("--")

price=int(input("Enter the item's price (no $ sign): "))

time.sleep(2)

print("You are...")
print(balance / price * 100)
print("%  To the way there!")

