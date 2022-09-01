def separator(rng):
    return '' if len(rng) == 1 else ',' if len(rng) == 2 else '-'


def rangefinder(r):
    rng, intervals = [], []
    for i in r:
        if len(rng) == 0 or i == max(rng) + 1:
            rng.append(i)
        else:
            intervals.append(f'{min(rng)}' if len(rng) == 1 else f'{min(rng)}{separator(rng)}{max(rng)}')
            rng = [i]
    intervals.append(f'{min(rng)}' if len(rng) == 1 else f'{min(rng)}{separator(rng)}{max(rng)}')

    return ','.join(intervals)
