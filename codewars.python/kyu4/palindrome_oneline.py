"""
https://www.codewars.com/kata/58b57f984f353b3dc9000030/python
"""


# Kata solution below
# palindrome = lambda n, s: (s * n)[:n // 2] + (s * n)[~-n // 2::-1]
def palindrome(num: int, letters: str) -> str:
    return (letters * num)[:num // 2] + (letters * num)[~-num // 2::-1]
