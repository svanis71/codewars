def next_smaller(n):
    digits = [int(c) for c in str(n)]
    if n < 21 or digits == sorted(digits):
        return -1
    result, first_smallest_pos, next_smallest_pos, next_smallest = [], len(digits) - 1, -1, -1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            first_smallest_pos -= 1
            break
        first_smallest_pos -= 1

    for i in range(first_smallest_pos, len(digits)):
        if digits[i] < digits[first_smallest_pos] and digits[i] > next_smallest:
            next_smallest = digits[i]
            next_smallest_pos = i

    digits[first_smallest_pos], digits[next_smallest_pos] = digits[next_smallest_pos], digits[first_smallest_pos]
    tail = sorted(digits[first_smallest_pos + 1:], reverse=True)
    result = [*digits[0:first_smallest_pos + 1], *tail]
    return int(''.join(str(x) for x in result)) if result[0] > 0 else -1
