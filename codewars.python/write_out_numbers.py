#
# https://www.codewars.com/kata/52724507b149fa120600031d/train/python
#

numbers: dict[int, str] = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                           8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                           14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                           19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                           70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}


def hundreds(n: int) -> tuple:
    a, n = divmod(n, 100)
    return (f'{numbers[a]} hundred ' if a > 0 else ''), n


def tens(n) -> str:
    if n < 21:
        return numbers[n] if n > 0 else ''
    t, ones = divmod(n, 10)
    return f'{numbers[t * 10]}{"" if ones == 0 else "-"}{"" if ones == 0 else numbers[ones]}'


def number2words(n: int) -> str:
    if n == 0:
        return 'zero'
    p1, p2 = divmod(n, 1000)
    s1, p1 = hundreds(p1)
    s2, p2 = hundreds(p2)
    s1 += tens(p1)
    s2 += tens(p2)
    return f'{s1.strip()}{" thousand " if len(s1) > 0 else ""}{s2}'.strip()
