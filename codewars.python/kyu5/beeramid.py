"""
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/python
"""


def beeramid(bonus: int, beer_price: float) -> int:
    if bonus <= 0:
        return 0
    beers_available: float = bonus / beer_price
    lvl: int = 1
    while beers_available >= lvl * lvl:
        beers_available -= (lvl * lvl)
        lvl += 1
    return lvl - 1
