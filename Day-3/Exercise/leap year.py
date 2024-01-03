"""Write a A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400."""

year = int(input("Enter the year: "))

if year % 4==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
        print("Not leap year")
else:
    print("Not leap year")