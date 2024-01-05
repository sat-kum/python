"""write a program that calculate the sum of all the even number from 1 to 1000.
if X is 100 then the even number would be 2 and the last one is 100."""


target = int(input("Enter a number for the range: "))

even_sum =0
for i in range(2, target+1, 2):
    even_sum+=i
    
print(even_sum)


## Alternative 

even_sum =0
for i in range(1, target+1):
    if i %2 ==0:
        even_sum+=i

print(even_sum)