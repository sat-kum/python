print("welcome to Treasure Island. \nYour mission is to find the teasure.")

choice1 = input("You`re at a cross road. where do you want to go? Type 'left' or 'right': ").lower()


if choice1 =='left':
    lake = input("you come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across: ").lower()
    if lake =='wait':
        door = input("you arrive at the island unharmed. There is a house with 3 door. One red, one yellow and one blue. which colour do you choose? ").lower()
        if door =="red":
            print("It`s a room full of fire. Game Over.")
        elif door == 'yellow':
            print("you found the treasure! you win!")
        elif door =='blue':
            print('you enter a room of beasts. Game Over.')
        else:
            print("you chose a door that doesn`t exist. Game Over.")
    else:
        print("you got attacked by an angry trout. Game Over.")
else:
    print("you fell into a hole. Game Over.")

