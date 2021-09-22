# https://www.codewars.com/kata/5a7778790136a132a00000c1/solutions/python
def single_digit(n):
    return n if n < 10 else single_digit(bin(n).count('1'))
