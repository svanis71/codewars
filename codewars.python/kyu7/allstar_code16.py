"""
    https://www.codewars.com/kata/586566b773bd9cbe2b000013/python
"""


def no_repeat(s: str) -> str:
    return [c for c in s if s.count(c) == 1].pop(0)
