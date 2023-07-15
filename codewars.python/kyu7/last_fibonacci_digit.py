"""
https://www.codewars.com/kata/56b7251b81290caf76000978
"""


def get_last_digit(n: int) -> int:
    if n < 3:
        return 1
    n1, n2 = 1, 1
    for _ in range(3, n + 1):
        n1, n2 = n2, n1 + n2
    return n2 % 10
