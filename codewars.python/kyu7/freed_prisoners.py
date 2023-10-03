"""
https://www.codewars.com/kata/6507e3170b7009117e0c7865/python
"""


def freed_prisoners(prisoners: list[bool]) -> int:
    if not prisoners[0]:
        return 0
    cnt = 0
    while len(prisoners) > 0:
        cnt += (1 if prisoners[0] else 0)
        prisoners = [not status for status in prisoners]
        while True:
            if len(prisoners) == 0 or prisoners[0]:
                break
            prisoners.pop(0)

    return cnt
