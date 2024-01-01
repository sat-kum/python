"""Create a program using math and f-string that tells us how many weeks we have left, if we live until 90 year old
it will take your current age as the input and output a message with our time left in this format 

you have X weeks left

where X is replace with the actual calculate number of weeks the input age has left until age 90
"""

age = int(input('Enter the your current age: '))

year = 90 - age

weeks = year*52

print(f"you have {weeks} weeks left.")
