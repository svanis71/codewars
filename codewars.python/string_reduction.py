# https://www.codewars.com/kata/59fab1f0c9fc0e7cd4000072/python
def reduce_string(a, b):
    return len(a) - len(b) if len([c for c in set(b) if a.count(c) < b.count(c)]) == 0 else 0
