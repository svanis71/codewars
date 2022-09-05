"""
https://www.codewars.com/kata/54e320dcebe1e583250008fd/train/python/6130609ceb26c1001a5f060d
"""
from math import factorial


def dec_2_fact_string(nb):
    cnt, letter_list = 1, []
    while nb > 0:
        nb, r = divmod(nb, cnt)
        letter_list.insert(0, str(r) if r < 10 else chr(55 + r))
        cnt += 1
    return ''.join(letter_list)


def fact_string_2_dec(s):
    return sum([int(c if ord(c) < 65 else ord(c) - 55) * factorial(i) for i, c in enumerate(s[::-1])])
