def alphabet_war_reinforces(reinforces, airstrikes):
    """
        https://www.codewars.com/kata/593e2077edf0d3e2d500002d

    :param reinforces:
    :param airstrikes:
    :return:
    """
    battlefield = reinforces.pop(0)
    for airstrike in airstrikes:
        bombs = [i for i, ch in enumerate(airstrike) if ch == '*']
        for pos in bombs:
            removefrom = 0 if pos == 0 else pos - 1
            removeto = pos if pos == len(battlefield) - 1 else pos + 1
            n = removeto - removefrom + 1
            battlefield = battlefield[:removefrom] + '_' * n + battlefield[removeto + 1:]

        reinforced_string = ''
        for pos, ch in enumerate(battlefield):
            rch = ch
            if ch == '_':
                for idx, ri in enumerate(reinforces):
                    if ri[pos] != '_':
                        rch = ri[pos]
                        reinforces[idx] = reinforces[idx][:pos] + '_' + reinforces[idx][pos + 1:]
                        break
            reinforced_string += rch
        battlefield = reinforced_string
    return battlefield

