# ClydeBank Coffee Shop Simulator 4000

# Copyright (c) 2024 ClydeBank Software Ltd. All rights reserved.

# Current day number

day = 1

# Sales list of dictionaries

# sales = [
#     {
#         "day": 1,
#         "coffee_env": 100,
#         "advertising": "10",
#         "temperature": 68,
#         "cups_sold": 16
#     },
#     {
#         "day": 2,
#         "coffee_env": 84,
#         "advertising": "15",
#         "temperature": 72,
#         "cups_sold": 20
#     },
#     {
#         "day": 3,
#         "coffee_env": 64,
#         "advertising": "5",
#         "temperature": 78,
#         "cups_sold": 10
#     }
# ]

# Create an empty sale list
sales = []

# Print welsome message
print("ClydeBank Coffee Shop Simulator 4000, Version 1.0")
print("Copyright (c) 2024 ClydeBank Software Ltd. All rights reserved.\n")
print("Let's collect some information before we start the game.!\n")


# Get name and shop name
name = input("What is your name? ")
shop_name = input("What is the name of your coffee shop? ")


print("\nThank you, " + name + ". Let's set some initial pricing'.\n")


# Get initial pricing of a cup of coffee
cup_price = input("What do you want to charge for a cup of coffee? $")


# Display what we have
print("\nGreat! Here is what we have collected so far:")
print("Your name is  " + name + " and you're opening " + shop_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + "\n")