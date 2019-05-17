def fib(n):
    fib0 = 0
    fib1 = 1
    fib = 0
    for i in range(n-1):
        fib = fib1 + fib0
        fib0 = fib1
        fib1 = fib
    return fib

def fibSlow(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))