"""
https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python
"""


def validate_word(word: str):
    word = word.lower()
    return len(set(word.count(c) for c in (set(word)))) == 1
