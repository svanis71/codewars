import re


def alphabet_war2(f):
    lefts, rights = ('wpbs', 'mqdz')
    replacer = lambda x : ''          # '*' if x.group(0)[-1] == '*' else ''
    fight = re.sub(r'[a-z]?\*[a-z]?', replacer, f)
    while fight.find('*') > -1:
        fight = re.sub(r'[a-z]?\*[a-z]?', replacer, fight)
    score_right = sum([4 - rights.find(x) for x in fight if x in rights])
    score_left = sum([4 - lefts.find(x) for x in fight if x in lefts])

    return ['Let\'s fight again!', ['Right side wins!', 'Left side wins!'][score_left > score_right]][score_right != score_left]