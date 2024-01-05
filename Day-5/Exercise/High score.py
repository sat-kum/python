"""Write a program that calculate the highest score from a list of score
**Don`t use max and min funtion.
"""


student_score = input("Enter the scores: ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

highest_score = 0
for sc in student_score:
    if sc > highest_score:
        highest_score=sc

print(f"The highest score in the class is: {highest_score}")