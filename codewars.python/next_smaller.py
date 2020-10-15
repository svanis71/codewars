import itertools


def next_smaller(n):
    # digits = list(str(n))
    # ordered = sorted(digits)
    # exists_smaller = ''.join(ordered) < ''.join(digits) and ordered[0] != 0
    # if n < 21 or not exists_smaller:
    #     return -1
    # for i in range(len(digits)):

    return n


    # digits = [x for x in str(n)]
    # numbers = sorted(
    #     [int(''.join(x)) for x in itertools.permutations(digits, len(digits)) if x[0] != '0' and x[0] <= digits[0]])
    # nextsmaller = [x for x in numbers if x < n]
    # return -1 if len(nextsmaller) == 0 else max(nextsmaller)
