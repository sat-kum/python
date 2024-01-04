### Bank Roulette  ######

"""you are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody`s food bill.

* Important: you are not allowed to use the choice() function.

Line 1 split the string names_string into individual names and puts them inside a list called names. For this to work, you must enter all the names as names followed by comma the space e.g. name, name, name

HINT: input : x,y,z. name = ['x', 'y', 'z']

"""

import random

name_string = input("Enter the names: ")
name = name_string.split(", ")


num_name= len(name)

random_choice = random.randint(0, num_name-1)

person = name[random_choice]

print(person + " is going to buy the food!!")