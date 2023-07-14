import unittest


def is_ship_at(battlefield: list[list[str]], xpos: int, ypos: int,
               shiptype: str, shiplength: int) -> tuple[bool, list[list[str]]]:
    new_field: list[list[str]] = [list(row) for row in battlefield]
    horiz = ''.join(battlefield[ypos][xpos: xpos + shiplength])
    vert = ''.join(r[xpos] for r in battlefield[ypos: ypos + shiplength])
    is_a_battlefield: bool = False
    if horiz == '1' * shiplength:
        above = ''.join(battlefield[ypos - 1][xpos - 1: xpos + shiplength + 1])
        below = ''.join(battlefield[ypos + 1][xpos - 1: xpos + shiplength + 1])
        if above == '0' * (shiplength + 2) and below == '0' * (shiplength + 2) and battlefield[ypos][
            xpos - 1] == '0' and \
                battlefield[ypos][xpos + shiplength] == '0':
            for xr in range(shiplength):
                new_field[ypos][xpos + xr] = shiptype
            is_a_battlefield = True
    if vert == '1' * shiplength:
        leftside = ''.join(r[xpos - 1] for r in battlefield[ypos - 1: ypos + shiplength + 1])
        rightside = ''.join(r[xpos + 1] for r in battlefield[ypos - 1: ypos + shiplength + 1])
        if leftside == '0' * (shiplength + 2) and rightside == '0' * (shiplength + 2) and battlefield[ypos - 1][
            xpos] == '0' and \
                battlefield[ypos + shiplength][xpos] == '0':
            for yr in range(shiplength):
                new_field[ypos + yr][xpos] = shiptype
            is_a_battlefield = True
    return is_a_battlefield, new_field


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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        battlefield = [[1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(validate_battlefield(battlefield), True)

    def test_somethingelse(self):
        battlefield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(validate_battlefield(battlefield), True)

    def test_should_return_false_if_contact(self):
        battlefield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(validate_battlefield(battlefield), False)


if __name__ == '__main__':
    unittest.main()
