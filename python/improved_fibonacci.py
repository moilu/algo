memo = {0: 0, 1: 1}


def improved_fib(n):
    if n not in memo:
        memo[n] = improved_fib(n - 1) + improved_fib(n - 2)
    return memo[n]


def print_fibonacci_sequence(n):
    for i in range(n + 1):
        print(improved_fib(i))


print_fibonacci_sequence(50)
