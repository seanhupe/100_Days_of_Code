
# Display art
from art import logo
from game_data import data
import random

print(logo)

def format_data(account):
    """Format account data: Display name, description, country"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


# Generate a random account from the game data file
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:              # in case they are the same
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")

# Ask user for a guess

# Check if user is correct
## Get follower count of each account
## Use if statement to check if user is correct

# Give user feedback on their guess

# Score Keeping

# Make game repeatable

# Make account at position B become the next account at position A


import random




