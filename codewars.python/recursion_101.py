def solve(a, b):
    #    while a != 0 and b != 0:
    if a >= b * 2:
        # a = a - 2 * b
        return [b + 1, a]
    elif b >= a * 2:
        b = b - 2 * a
    else:
        return [a, b]

#    return [a, b]
