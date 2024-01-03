"""Write a program that test the compatibility between two people."""


name1 = input('what is your name? ')
name2 = input('what is their name? ')

com_name = (name1+name2).lower()
print(com_name)

#true love
t= com_name.count('t')
r= com_name.count('r')
u = com_name.count('u')
e = com_name.count('e')

first_digit = t+r+u+e

l = com_name.count('l')
o = com_name.count('o')
v = com_name.count('v')
e = com_name.count('e')

second_digit = l+o+v+e

com_digit = int(str(first_digit)+ str(second_digit))

if (com_digit >10) and (com_digit >90):
    print(f"your score is {com_digit}, you go together like coke and mentos")
elif (com_digit >=40) and (com_digit<=50):
    print(f"your score is {com_digit}, you are alright together.")
else:
    print(f"your score is {com_digit}")