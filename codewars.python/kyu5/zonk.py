def is_x_of_a_kind(x: int, diceval: int, dice: list[int]) -> tuple[int, list[int]]:
    if sum(i for i in dice if i == diceval) == x * diceval:
        return (
            ((1000 * (x - 2)) if diceval == 1 else (diceval * 100 * (x - 2))),
            [n for n in dice if n != diceval])
    return 0, dice


def get_score(dice: list[int]) -> int:
    score = 0
    # Straight (1,2,3,4,5 and 6)	6 3 1 2 5 4	1000 points
    sorted_dice = sorted(dice)
    if sorted_dice == [1, 2, 3, 4, 5, 6]:
        return 1000
    # Four of a kind	1 1 1 1 4 6	 2 × Three-of-a-kind score (in example, 2000 pts)
    # Five of a kind	5 5 5 4 5 5	 3 × Three-of-a-kind score (in example, 1500 pts)
    # Six of a kind	4 4 4 4 4 4	 4 × Three-of-a-kind score (in example, 1600 pts)
    # Three of 1	1 4 1 1	1000 points
    # Three of 2	2 3 4 2 2	200 points
    # Three of 3	3 4 3 6 3 2	300 points
    # Three of 4	4 4 4	400 points
    # Three of 5	2 5 5 5 4	500 points
    # Three of 6	6 6 2 6	600 points
    for nof in range(6, 2, -1):
        for n in range(1, 7):
            sc, sorted_dice = is_x_of_a_kind(nof, n, sorted_dice)
            score += sc

    # Three pairs of any dice	2 2 4 4 1 1	750 points
    if len([(d1, d2) for (d1, d2) in zip(sorted_dice, sorted_dice[1::]) if d1 == d2]) == 3:
        return 750

    # Every 1	4 3 1 2 2	100 points
    # Every 5	5 2 6	50 points
    score += (sorted_dice.count(1) * 100)
    score += (sorted_dice.count(5) * 50)

    return score
