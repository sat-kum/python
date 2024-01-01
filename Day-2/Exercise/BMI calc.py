""" Write a program that calculates the Body Mass Index(BMI) from a user`s weight and height

BMI = weight(kg)/(Height**2(m2))

"""

height = float(input("Enter the your Height(m2): "))

weight = int(input("Enter the your Weight(kg): "))

BMI = weight/(height**2)

print("your BMI is: ", BMI)