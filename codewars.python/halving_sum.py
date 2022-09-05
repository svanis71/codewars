"""
https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python/61305d143b5bb90032b47a4b
"""


def halving_sum(n):
    a = []
    while n >= 1:
        a.append(n)
        n = int(n / 2)
    return sum(a)
