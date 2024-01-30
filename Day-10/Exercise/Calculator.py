#Calculator

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiple (n1, n2):
    return n1 * n2

#Divide
def divide (n1 , n2):
    return n1/n2

operation = {"+": add, "-": subtract, "*": multiple, "/": divide}

num1 = int(input("What's the first number?: "))

for symbol in operation:
    print(symbol)

operation_symbol = input("pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

Calculation_function = operation[operation_symbol]
answer = Calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")