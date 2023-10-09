"""
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
"""


def print_spiral(spiral: list[list[int]], cx, cy):
    print(f'y: {cy}, x:{cx}')
    for _, r in enumerate(spiral):
        for _, c in enumerate(r):
            print(f'{"." if c == 0 else "+"}', end='')
        print()
    print(f'\n{"-" * len(spiral)}\n')


def valid_move(spiral: list[list[int]], to_x: int, to_y: int, dir_x: int, dir_y: int) -> bool:
    if dir_x != 0 and (
            is_visited(spiral, to_y - 1, to_x) or is_visited(spiral, to_y + 1, to_x) or is_visited(spiral, to_y,
                                                                                                   to_x + dir_x)):
        return False
    if dir_y != 0 and (
            is_visited(spiral, to_y, to_x - 1) or is_visited(spiral, to_y, to_x + 1) or is_visited(spiral, to_y + dir_y,
                                                                                                   to_x)):
        return False
    return True


def is_visited(spiral: list[list[int]], y: int, x: int) -> bool:
    if x < 0 or y < 0:
        return False
    if 0 <= x < len(spiral) and 0 <= y < len(spiral):
        return spiral[y][x] == 1
    return False


def spiralize(size: int) -> list[list[int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    spiral = [[0 for _ in range(size)] for _ in range(size)]
    cx, cy, edge_x, edge_y = 0, 0, size - 1, size - 1
    dx, dy = directions[0]

    while valid_move(spiral, cx, cy, dx, dy):
        spiral[cy][cx] = 1
        if (dx > 0 and cx >= edge_x) or (dy > 0 and cy >= edge_y):
            directions.append(directions.pop(0))
        elif (dx < 0 and cx == 0) or (dy < 0 and cy == 0):
            directions.append(directions.pop(0))
        elif is_visited(spiral, cy + dy * 2, cx + dx * 2):
            directions.append(directions.pop(0))
        dy, dx = directions[0]
        cx += dx
        cy += dy
    print_spiral(spiral, cx, cy)

    return spiral
