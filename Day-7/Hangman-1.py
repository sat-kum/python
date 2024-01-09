# create a program for the Hangman

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
word_list = ["aardvark", "baboon", "camel"]

chose_word = random.choice(word_list)

guess = input("Guess the letter: ").lower()


for i in chose_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")

