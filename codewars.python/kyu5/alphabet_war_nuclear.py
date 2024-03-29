import re


def alphabet_war_nuclear(battlefield):
    if battlefield.find('#') < 0:
        return battlefield.replace('[', '').replace(']', '')

    groups = [x for x in re.split(r'(\[?[a-z#]+]?)', battlefield) if x != '']
    survivors = ''
    bombs = 0
    for x, group in enumerate(groups):
        bombs += len(re.findall('#', group))
        if group.find('[') > -1:
            if x + 1 < len(groups):
                bombs += len(re.findall('#', groups[x + 1]))
            if bombs < 2:
                survivors += group[1:-1]
            bombs = 0

    return survivors
