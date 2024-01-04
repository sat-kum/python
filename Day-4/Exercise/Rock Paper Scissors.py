"""Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player. """


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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

user = int(input("what do you choose? Type 0 for Rock, or 1 or Paper or 2 for Scissors. "))

if user >= 3 or user<0:
    print('You typed an invalid number, you lose!')

else:
    print(game_image[user])
    comp_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_image[comp_choice])

    if user ==0 and comp_choice ==2:
        print('you win')
    elif comp_choice == 0 and user ==2:
        print('you lose')
    elif comp_choice > user:
        print('you lose')
    elif user > comp_choice:
        print("you win!!")
    elif comp_choice == user:
        print("It's a draw")
