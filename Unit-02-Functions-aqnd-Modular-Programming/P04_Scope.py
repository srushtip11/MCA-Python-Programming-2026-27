x = 10

def display():
    global x
    y = 20
    print("Global variable:", x)
    print("Local variable:", y)
    x = 30

display()
print("Modified global variable:", x)

square = lambda a: a * a
cube = lambda a: a * a * a
maximum = lambda a, b: max(a, b)
addition = lambda a, b: a + b

print("Square:", square(5))
print("Cube:", cube(3))
print("Maximum:", maximum(10, 20))
print("Addition:", addition(10, 20))