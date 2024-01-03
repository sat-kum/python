"""Write a program for BMI based on the user height and weight if the BMI 
under 18.5 - you are underweight
over 18.5 but below 25 they have a normal weight
over 25 but below 30 they  are slightly overweight
over 30 but below 35 they are obese
above 35 they are clinically obese"""


height = float(input("Enter your height in meters: "))

weight =int(input("Enter your weight in kilogram: "))

BMI = weight/height**2

if BMI <=18.5:
    print( f"your BMI is {BMI} you are underweight")
elif BMI <=25:
    print(f"your BMI is {BMI} you have a normal weight")
elif BMI <=30:
    print(f"your BMI is {BMI} you are slightly overweight")
elif BMI <=35:
    print(f"your BMI is {BMI} you are obese")
else:
    print(f"your BMI is {BMI} you are clinically obese")