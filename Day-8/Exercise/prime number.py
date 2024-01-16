# Need to write a function that checks wheather if the number passed into it is a prime number or not.


def prime_num(num):
    
    is_prime = True
    for i in range(2, num):
        if num % i ==0:
            is_prime = False
    if is_prime:
        print("It`s a prime number.")
    else:
        print("It`s not a prime number.")


n = int(input("Enter the number: "))
prime_num(num = n)