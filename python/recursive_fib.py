def recursive_fib(n):
    if n < 2:
        return n
    return recursive_fib(n - 2) + recursive_fib(n - 1)


def print_fibonacci_sequence(n):
    for i in range(n + 1):
        print(recursive_fib(i))


print_fibonacci_sequence(5)
