import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)

# Iterate over the string
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
