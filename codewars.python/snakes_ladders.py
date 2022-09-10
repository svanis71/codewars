SNAKES_LADDERS = dict(
    [(99, 80), (95, 75), (92, 88), (89, 68), (74, 53), (62, 19), (64, 60), (46, 25), (49, 11), (16, 6),
     (2, 38), (7, 14), (8, 31), (15, 26), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (78, 98),
     (87, 94)])


class SnakesLadders:
    def __init__(self):
        self.gameActive = True
        self.activePlayer = 1
        self.players_positions = [0, 0]

    def move(self, steps):
        move_to = self.players_positions[0] + steps
        move_to = move_to if move_to <= 100 else 100 + (100 - move_to)
        move_to = move_to if move_to not in SNAKES_LADDERS else SNAKES_LADDERS[move_to]
        self.players_positions[0] = move_to
        return move_to

    def play(self, die1, die2):
        if not self.gameActive:
            return "Game over!"
        player = self.activePlayer
        next_pos = self.move(die1 + die2)
        self.gameActive = next_pos != 100
        if die1 != die2:
            self.activePlayer = 3 - self.activePlayer
            self.players_positions.append(self.players_positions.pop(0))
        return f"Player {player} Wins!" if next_pos == 100 else f"Player {player} is on square {next_pos}"
