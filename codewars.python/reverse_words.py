import re

'''
Reverse Words

https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
'''


def reverse_words(s):
    return ''.join([w[::-1] for w in re.findall(r'[^\s]+|\s+', s)])
