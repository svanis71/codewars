"""
    https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf/python
"""


def cat_mouse(x: str, j: int) -> str:
    if any(x.find(c) == -1 for c in 'CDm'):
        return 'boring without all three'
    if abs(x.index('C') - x.index('m')) > j + 1:
        return 'Escaped!'
    return 'Protected!' if x.replace('.', '')[1] == 'D' else 'Caught!'
