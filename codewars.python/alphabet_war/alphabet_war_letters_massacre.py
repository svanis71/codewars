import re


def alphabet_war_letters_massacre(fight):
    """
    https://www.codewars.com/kata/5938f5b606c3033f4700015a
    :param fight:
    :return:
    """
    lefts, rights = ('wpbs', 'mqdz')
    fight = re.sub(r'[a-z]?\*[a-z]?', '', fight)
    points_right = sum([4 - rights.find(x) for x in fight if x in rights])
    points_left = sum([4 - lefts.find(x) for x in fight if x in lefts])

    if points_right == points_left:
        return 'Let\'s fight again!'
    return 'Right side wins!' if points_right > points_left else 'Left side wins!'
