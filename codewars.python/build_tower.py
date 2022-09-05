"""
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
"""


def tower_builder(n_floors):
    return [('*' * i).center(n_floors * 2 - 1, ' ') for i in range(1, n_floors * 2, 2)]
