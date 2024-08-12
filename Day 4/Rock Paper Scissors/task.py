import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_______
          _________)
          __________)
         __________)
---._____________)
'''

scissors = '''
    _______
---'   ____)_______
          _________)
       _____________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
print("You Chose:")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid number - you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You LOSER!")

elif user_choice > computer_choice:
    print("You WIN!")

elif computer_choice == user_choice:
    print("It is a Draw - Play again!")

elif computer_choice == 0 and user_choice == 2:
    print("LOSER!")



