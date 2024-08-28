from art import logo
from random import randint
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too Low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = (input("Choose a difficulty. Type 'easy' or 'hard': "))
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



# Choose a random number 1 - 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)
print(f"Pssst, the correct answer is{answer}")



# Let the user guess a number
int(input("Make a guess: "))
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")



# Track number of turns/guesses and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong
