def next_smaller(n):
    digits = [int(c) for c in str(n)]
    ordered = sorted(digits)
    if n < 21 or digits == ordered:
        return -1
    # Börja från höger och hitta första siffran där vänster > höger
    for idx, (left, right) in enumerate(zip(digits, digits[1:])):
        if left > right:
            pass

    return n

    # digits = [x for x in str(n)]
    # numbers = sorted(
    #     [int(''.join(x)) for x in itertools.permutations(digits, len(digits)) if x[0] != '0' and x[0] <= digits[0]])
    # nextsmaller = [x for x in numbers if x < n]
    # return -1 if len(nextsmaller) == 0 else max(nextsmaller)
