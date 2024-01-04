### write a virutal coin toss program. it will randomly tell the user "head" or "tail"

## you should generate a random number, either 0 or 1. Then use that number to print out "Head" or "Tail"


import random

toss = random.randint(0,1)

if toss == 1:
    print("Heads")
else:
    print("Tails")