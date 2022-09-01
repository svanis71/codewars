'''
https://www.codewars.com/kata/58b57f984f353b3dc9000030/python
'''
palindrome = lambda n, s: (s * n)[:n // 2] + (s * n)[~-n // 2::-1]
