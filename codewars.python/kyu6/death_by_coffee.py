"""
https://www.codewars.com/kata/57db78d3b43dfab59c001abe/python
"""


def find_limit(healthnumber: int, to_add: int) -> int:
    hn_hex, cups = '', 0
    while cups < 5000 and 'dead' not in hn_hex:
        cups += 1
        healthnumber += to_add
        hn_hex: str = hex(healthnumber)[2:]
    return 0 if cups >= 5000 else cups


def coffee_limits(y: int, m: int, d: int) -> list[int]:
    hn: int = int(f'{y:04}{m:02}{d:02}')
    return [find_limit(hn, 0xcafe), find_limit(hn, 0xdecaf)]
