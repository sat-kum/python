"""Write a program that calculate the average student height from a list of height"""


height = input("Student height: ").split()

for n in range(0, len(height)):
    height[n]= int(height[n])

total_height =0
total_num =0
for hi in height:
    total_height +=hi
    total_num +=1

print(f"total height = {total_height}")
print(f"Number of student = {total_num}")

avg_height= round(total_height/total_num)
print(f"average height ={avg_height}")