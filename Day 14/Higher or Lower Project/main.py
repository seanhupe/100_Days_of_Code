
# Display art
from art import logo, vs
from game_data import data
import random



def format_data(account):
    """Format account data to be printable: Display name, description, country"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower accounts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"        # if user guessed a, then return True
    else:
        return guess == "b"         # if user guess b, then return True


print(logo)
score = 0

# Generate a random account from the game data file
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:                      # in case they are the same
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)                                       # Pring the VS ASC art
print(f"Against B: {format_data(account_b)}.")

# Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
## Get follower count of each account
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)


## Use if statement to check if user is correct

# Give user feedback on their guess
# Score Keeping
if is_correct:
    score += 1
    print(f"You're right! Current score {score}")
else:
    print(f"Sorry, that is wrong. Final Score {score}")



# Make game repeatable

# Make account at position B become the next account at position A







