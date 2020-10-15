def test_hamming_candidate(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return test_hamming_candidate(n / 2)
    if n % 3 == 0:
        return test_hamming_candidate(n / 3)
    if n % 5 == 0:
        return test_hamming_candidate(n / 5)
    return False


def hamming_numbers():
    n = 1
    while True:
        if test_hamming_candidate(n):
            yield n
        n += 1


def hamming(n):
    for i, x in enumerate(hamming_numbers()):
        if i + 1 == n:
            return x

def h(n):
    pass