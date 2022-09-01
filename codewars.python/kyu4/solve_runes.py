import re

OP = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}


def solve_runes(s):
    for i in '0123456789':
        if i not in s:
            t = s.replace('?', i)
            n1, op, n2, eq = re.findall(r'(-?[\d]+)([*+-])(-?[\d]+)[=](-?[\d]+)', t)[0]
            if not re.search(r'^-?0\d+', n1) and not re.search(r'^-?0\d+', n2) and not re.search(r'^-?0\d+', eq):
                if OP[op](int(n1), int(n2)) == int(eq):
                    return int(i)
    return -1
