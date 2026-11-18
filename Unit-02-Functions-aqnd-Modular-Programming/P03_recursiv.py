def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = 5

print("Factorial:", factorial(num))

print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")