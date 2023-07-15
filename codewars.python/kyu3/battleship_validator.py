"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/python
"""


def is_ship_at(battlefield: list[list[str]], xpos: int, ypos: int,
               shiptype: str, shiplength: int) -> tuple[bool, list[list[str]]]:
    new_field: list[list[str]] = [list(row) for row in battlefield]
    horiz = ''.join(battlefield[ypos][xpos: xpos + shiplength])
    vert = ''.join(r[xpos] for r in battlefield[ypos: ypos + shiplength])
    is_a_battlefield: bool = False
    if horiz == '1' * shiplength:
        has_no_contact = no_horizontal_contact(battlefield, shiplength, xpos, ypos)
        if has_no_contact:
            for xr in range(shiplength):
                new_field[ypos][xpos + xr] = shiptype
            is_a_battlefield = True
    if vert == '1' * shiplength:
        has_no_c_contact = has_no_vertical_contact(battlefield, shiplength, xpos, ypos)
        if has_no_c_contact:
            for yr in range(shiplength):
                new_field[ypos + yr][xpos] = shiptype
            is_a_battlefield = True
    return is_a_battlefield, new_field


def has_no_vertical_contact(battlefield, shiplength, xpos, ypos):
    leftside = ''.join(r[xpos - 1] for r in battlefield[ypos - 1: ypos + shiplength + 1])
    rightside = ''.join(r[xpos + 1] for r in battlefield[ypos - 1: ypos + shiplength + 1])
    outside_len = shiplength + 2
    free_space_needed = '0' * outside_len
    return leftside == free_space_needed and rightside == free_space_needed and battlefield[ypos - 1][xpos] == '0' and \
        battlefield[ypos + shiplength][xpos] == '0'


def no_horizontal_contact(battlefield, shiplength, xpos, ypos):
    above = ''.join(battlefield[ypos - 1][xpos - 1: xpos + shiplength + 1])
    below = ''.join(battlefield[ypos + 1][xpos - 1: xpos + shiplength + 1])
    outside_len = shiplength + 2
    free_space_needed = '0' * outside_len
    return above == free_space_needed and below == free_space_needed and battlefield[ypos][xpos - 1] == '0' and \
        battlefield[ypos][xpos + shiplength] == '0'


def validate_battlefield(field: list[list[int]]):
    battlefield: list[list[str]] = [['0'] + [str(c) for c in row] + ['0'] for row in field]
    battlefield.insert(0, ['0'] * (len(field[0]) + 2))
    battlefield.append(['0'] * (len(field[0]) + 2))
    shiptypes = 'BCDS'
    shiptype_count = [0, 0, 0, 0]
    for y, row in enumerate(battlefield):
        for x, _ in enumerate(row):
            for idx, shiptype in enumerate(shiptypes):
                is_it_a_ship, battlefield = is_ship_at(battlefield, x, y, shiptype, 4 - idx)
                if is_it_a_ship:
                    shiptype_count[idx] += 1
    battleships, cruisers, destroyers, submarines = shiptype_count
    return battleships == 1 and cruisers == 2 and destroyers == 3 and submarines == 4
