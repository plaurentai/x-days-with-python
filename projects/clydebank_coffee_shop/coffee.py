# ClydeBank Coffee Shop Simulator 4000
# Copyright (c) 2024 ClydeBank Software Ltd. All rights reserved.


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