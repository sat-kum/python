# Password Generator 
"""The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge."""


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password =""
#Easy level eg: gyf(*94
print('---Easy level---')

for char in range(1 , nr_letters+1):
    password +=random.choice(letters)

for char in range(1, nr_symbols+1):
    password += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password += random.choice(numbers)

print(password)

# Hardlevel
print('---Hard Level---')

password_list = []

for char in range(1 , nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

#print(password_list)
hard_pass =""

random.shuffle(password_list)
for i in password_list:
    hard_pass += i

print(hard_pass)
