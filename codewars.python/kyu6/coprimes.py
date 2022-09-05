from gcd import gcd


def coprimes(n):
    """
    https://www.codewars.com/kata/59e0dbb72a7acc3610000017/python
    :param n:
    :return:
    """
    return [k for k in range(n) if gcd(n, k) == 1]
