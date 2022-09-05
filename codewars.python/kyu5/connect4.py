class Connect4:
    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.currentPlayer = 2
        self.gameOver = False

    def play(self, col):
        if self.gameOver:
            return 'Game has finished!'

        free_rows = list(idx for idx, row in enumerate(self.board) if row[col] == 0)
        if len(free_rows) == 0:
            return "Column full!"

        self.currentPlayer = 3 - self.currentPlayer
        self.board[max(free_rows)][col] = self.currentPlayer
        self.gameOver = self.has_winner()

        return f'Player {self.currentPlayer} {"has a turn" if not self.gameOver else "wins!"}'

    def check_horizontal(self):
        return len([True for str_row in [''.join([str(c) for c in row]) for row in self.board] if
                    str_row.find('1111') >= 0 or str_row.find('2222') >= 0]) > 0

    def check_vertical(self):
        return len([True for vert in [''.join([str(x[col]) for x in self.board]) for col in range(7)] if
                    vert.find('1111') >= 0 or vert.find('2222') >= 0]) > 0

    def check_diagonal(self):
        return self.diagonal_left() or self.diagonal_right()

    def diagonal_right(self):
        b = self.board
        for x in range(4):
            for y in range(3):
                if b[y][x] != 0 and b[y][x] == b[y + 1][x + 1] and b[y][x] == b[y + 2][x + 2] \
                        and b[y][x] == b[y + 3][x + 3]:
                    return True
        return False

    def diagonal_left(self):
        b = self.board
        for x in range(3, 7):
            for y in range(3):
                if b[y][x] != 0 and b[y][x] == b[y + 1][x - 1] and b[y][x] == b[y + 2][x - 2] \
                        and b[y][x] == b[y + 3][x - 3]:
                    return True
        return False

    def has_winner(self):
        return self.check_horizontal() or self.check_vertical() or self.check_diagonal()
