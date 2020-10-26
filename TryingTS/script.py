def fib(n):
    # f(0), f(1) are 1, 1
    # rule is: f(n) = f(n-1) + f(n-2)
    # a, b = 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for inp in range(0,11):
    # print('inp: ',inp)
    print('fib: ',fib(inp))