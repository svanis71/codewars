"""
https://www.codewars.com/kata/57675f3dedc6f728ee000256/python
"""


def tower_builder(n_floors, block_size):
    w, h = block_size
    tower = []
    for floor in range(1, n_floors + 1):
        tower += [('*' * ((2 * floor - 1) * w)).center((2 * n_floors - 1) * w) for _ in range(h)]
    return tower
