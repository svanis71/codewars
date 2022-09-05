lefts, rights = ('wpbs', 'mqdz')
wooloo = {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z', 'm': 'w', 'q': 'p', 'd': 'b', 'z': 's'}


def is_priest(letter):
    return letter != '' and letter in 'jt'


def is_opponent(priest, letter):
    if priest == 'j':
        return letter in lefts
    return letter in rights


def is_between_priests(prev_p, next_p):
    return is_priest(prev_p) and is_priest(next_p) and prev_p != next_p


def alphabet_war_wooloo(fight):
    """
        https://www.codewars.com/kata/59473c0a952ac9b463000064

    :param fight:
    :return:
    """
    target = fight
    for i, letter in enumerate(fight):
        if letter in 'jt':
            continue
        prev = fight[i - 1 if i > 0 else 0]
        next_p = fight[i + 1:i + 2]
        if not is_between_priests(prev, next_p) and ((is_priest(prev) and is_opponent(prev, letter)) or (
                is_priest(next_p) and is_opponent(next_p, letter))):
            target = target[0:i] + wooloo[letter] + target[i + 1:]

    score_right = sum([4 - rights.find(x) for x in target if x in rights])
    score_left = sum([4 - lefts.find(x) for x in target if x in lefts])
    return ['Let\'s fight again!', ['Right side wins!', 'Left side wins!'][score_left > score_right]][
        score_right != score_left]


