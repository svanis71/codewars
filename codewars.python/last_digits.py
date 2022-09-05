"""
https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python
"""


def solution(n, d):
    last_digits = []
    while d > 0:
        n, r = divmod(n, 10)
        d -= 1
        last_digits.insert(0, r)
        if n == 0:
            break
    return last_digits
