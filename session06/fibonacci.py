def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(5))

def fact(n):
    if n== 1:
        return 1
    else: 
        return fact(n-1) * n 

print(fact(3))
