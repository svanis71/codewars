"""
    https://www.codewars.com/kata/65d2460f512ea70058594a3d/python
"""
from collections import Counter


def last_non_empty_string(string: str) -> str:
    cnt = dict(Counter(string))
    while any(True for k, v in cnt.items() if v > 1):
        cnt = {k: v - 1 for k, v in cnt.items() if v > 1}
    newstr = reversed(''.join(c for c in string if c in cnt.keys()))
    dest = ''
    while len(cnt.keys()) > 0:
        c = next(newstr)
        if c in cnt:
            dest += c
            del cnt[c]
    return dest[::-1]
