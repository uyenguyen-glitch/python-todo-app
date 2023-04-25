import random

# Get two numbers from the user and covert them to integers
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Pick a random int using randint()
number = random.randint(lower, upper)
print(number)