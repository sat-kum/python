# If the bill was $150.00, split between 5 people, with 12% tip
# Each person should pay(150.00/5)*1.12 = 33.6
# Round the result to 2 decimal places = 33.60

total = float(input("What was the total bill? $: "))

tip = int(input('How munch tip would you like to give 10,12 or 15?: '))

people = int( input('How many people to split the bill: '))

tip_per =tip/100
total_tip_amount = total+tip_per
total_bill = total+total_tip_amount
bill_per_person = total_bill/people

final_amount= round(bill_per_person, 2)

print(f"Each person should pay $ {final_amount}")