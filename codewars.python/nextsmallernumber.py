import itertools
import time


def next_smaller(n):
    digits = [x for x in str(n)]
    curr_min = n
    for i,c in enumerate(reversed(digits)):
        [int(''.join(x)) for x in itertools.permutations(digits, len(digits))]

    numbers = sorted(
        [int(''.join(x)) for x in itertools.permutations(digits, len(digits)) if x[0] != '0' and x[0] <= digits[0]])
    nextsmaller = [x for x in numbers if x < n]
    return -1 if len(nextsmaller) == 0 else max(nextsmaller)

