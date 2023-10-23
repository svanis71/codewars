def is_visited(spiral: list[list[int]], y: int, x: int) -> bool:
    if x < 0 or y < 0:
        return False
    if 0 <= x < len(spiral) and 0 <= y < len(spiral):
        return spiral[y][x] != 0
    return False


def create_spiral(size) -> list[list[int]]:
    if not str(size).isnumeric() or size < 1:
        return []
    spiral: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
    directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cx, cy, edge_x, edge_y = 0, 0, size - 1, size - 1
    dy, dx = directions[0]
    for i in range(size ** 2):
        spiral[cy][cx] = i + 1
        if (dx > 0 and cx >= edge_x) or (dy > 0 and cy >= edge_y):
            directions.append(directions.pop(0))
        elif (dx < 0 and cx == 0) or (dy < 0 and cy == 0):
            directions.append(directions.pop(0))
        elif is_visited(spiral, cy + dy, cx + dx):
            directions.append(directions.pop(0))
        dy, dx = directions[0]
        cx += dx
        cy += dy
    return spiral
