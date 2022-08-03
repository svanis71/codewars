def triangle(row):
    num_list = [0 if c == 'R' else 1 if c == 'G' else 2 for c in row]
    n = len(num_list) - 1
    result = 0
    for k, col in enumerate(num_list):
        if col != 0:
            result = (result + n_over_k_mod3(n, k) * col) % 3
    if n % 2 == 1:
        result = (- result) % 3
    return 'R' if result == 0 else 'G' if result == 1 else 'B'


def n_over_k_mod3(n, k):
    """ Compute the binomial coefficient C(n, k) modulo 3.

    It is assumed that 0 <= k <= n.

    The implementation uses Lucas's theorem, see for example
    https://en.wikipedia.org/wiki/Lucas%27s_theorem .
    """
    result = 1
    while n > 0:
        n3 = n % 3
        k3 = k % 3
        # 'Ad hoc' computation of C(n3, k3):
        if k3 > n3:
            return 0  # Return immediately if a factor is zero.
        if k3 != n3 and k3 != 0:
            result = (result * 2) % 3
        n = n // 3
        k = k // 3
    return result
