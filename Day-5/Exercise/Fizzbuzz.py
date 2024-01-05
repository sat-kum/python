## Write a program that print the solution to FizzBuzz game.

"""
1. your program should print each number from 1 to 100 in turn and include 100
2. the number is divisible by 3 then instead of printing the number it should print 'Fizz'.
3. when the number is divisible by 5 then instead of printing the number it should print 'Buzz'.
4. And if number  is divisible by 3 and 5 e.g. then instead of the number it should print 'FizzBuzz'.
"""

print("***FizzBuzz Game***")

target =100
for i in range(1, target+1):
    if (i % 3 ==0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)