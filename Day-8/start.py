# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.



def greet():
    print("hello")
    print("how are you")
    print("bye!!")

greet()


# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you doing {name}")

greet_with_name("Bean")

# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("lily","London")

#Function with keyword arguments
greet_with(location="Liverpool", name="Angela")