import random


def squares(n):
    return [i * i for i in range(1, n + 1)]


def num_range(n, start, step):
    if n <= 0:
        return []
    return list(range(start, start + step * n, step))


def rand_range(num_rands: int, min_value: int, max_value: int):
    nums = [random.SystemRandom().randint(min_value, max_value) for _ in range(num_rands)]
    return nums


def is_prime(test_num: int):
    if test_num % 2 == 0:
        return test_num == 2
    i = 3
    while i * i <= test_num:
        if test_num % i == 0:
            return False
        i += 2
    return True


def primes(num_primes: int):
    primes_list = [2] if num_primes >= 1 else []
    cnt, nx = len(primes_list), 3
    while cnt < num_primes:
        if is_prime(nx):
            primes_list.append(nx)
            cnt += 1
        nx += 2
    return primes_list
