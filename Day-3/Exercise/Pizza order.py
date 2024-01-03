"""create a program for pizza delivery
small size = $15
medium size = $20
large size = $25
add pepperoni for small  (Y or N)= $+2
add pepperoni for medium and large  (Y or N) = $+3
extra chess (Y or N)= $+1
"""

print("Thank you for choosing Pizza Delivery")

size= input("what size pizza do you want? S, M, or L: ")

add_pep = input("Do you want pepperoni? Y or N: ")

chess= input('Do you need extra chesses? Y or N: ')

bill = 0
if size =='S':
    bill +=15
elif size =='M':
    bill+=5
else :
    bill+=10

if add_pep =='Y':
    if size=='S':
        bill+=2
    else:
        bill +=3

if chess =="Y":
    bill+=1

print(f"your final bill is $ {bill}.")