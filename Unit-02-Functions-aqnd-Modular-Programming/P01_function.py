def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def operation(a, b, op="addition"):
    if op == "addition":
        return add(a, b)
    elif op == "subtraction":
        return subtract(a, b)
    elif op == "multiplication":
        return multiply(a, b)
    elif op == "division":
        return divide(a, b)

print("Addition:", operation(10, 5))
print("Subtraction:", operation(10, 5, op="subtraction"))
print("Multiplication:", operation(a=10, b=5, op="multiplication"))
print("Division:", operation(10, 5, op="division"))