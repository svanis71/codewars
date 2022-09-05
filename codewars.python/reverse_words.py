import re


def reverse_words(s):
    """
    https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
    :param s: input string
    :return: reversed string
    """
    return ''.join([w[::-1] for w in re.findall(r'[^\s]+|\s+', s)])
