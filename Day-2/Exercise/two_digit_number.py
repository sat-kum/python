""" write a program that adda the digit in a 2 digit number e.g. if the input was 35, then the output should be 3+5 =8

warning: do not change the the code on line 1. your programe should work for different inputs. eg. any two-digit number.

The last line of your program should print the result

Example 1 input :
39
Example 1 output:
12

Example 1 input :
43
Example 1 output:
7
"""

num = input('Enter two digit number: ')

first_digit = int(num[0])
second_digit = int(num[1])

two_digit_num = first_digit+second_digit
print(two_digit_num)

# alternative code line
print(int(num[0]) + int(num[1]))
