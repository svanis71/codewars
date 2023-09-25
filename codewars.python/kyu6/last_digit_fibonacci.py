"""
https://www.codewars.com/kata/56b7771481290cc283000f28
"""


def fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    n1, n2 = 1, 1
    for _ in range(3, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


def last_fib_digit(n):
    return [fib(n) % 10 for n in range(60)][n % 60]
