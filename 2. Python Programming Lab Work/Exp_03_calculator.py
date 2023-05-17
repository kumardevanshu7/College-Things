# Python Practical 03 : To write a python program  to create a calculator.

# create a operation function
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero!")
        return None
    return x / y

# taking user input
x = float(input("Type the first number: "))
operator = input("Select an operator (+, -, *, /): ")
y = float(input("Type the second number: "))

# Perform calculation
if operator == "+":
    ans = add(x, y)
elif operator == "-":
    ans = subtract(x, y)
elif operator == "*":
    ans = multiply(x, y)
elif operator == "/":
    ans = divide(x, y)
else:
    print("INVALID")
    ans = None

# Print the result
if ans is not None:
    print("Your Ans:", ans)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
