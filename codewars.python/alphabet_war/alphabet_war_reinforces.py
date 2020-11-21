def alphabet_war_reinforces(reinforces, airstrikes):
    """
        Doesn't work

        https://www.codewars.com/kata/593e2077edf0d3e2d500002d

    :param reinforces:
    :param airstrikes:
    :return:
    """
    battlefield = reinforces[0]
    for i, airstrike in enumerate(airstrikes):
        # strike
        pos = airstrike.find('*')
        removefrom = 0 if pos == 0 else pos - 1
        removeto = pos + 1
        n = removeto - removefrom
        battlefield = battlefield[0:removefrom] + '_'*n + battlefield[removeto:]
        # reinforce
        battlefield = reinforces
    return ''

