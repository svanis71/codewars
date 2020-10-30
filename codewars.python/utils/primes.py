def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 25:
        return True
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True


def generate_primes_to(n):
    return [2] if n == 2 else [2] + [p for p in range(3, n, 2) if is_prime(p)]


def get_next_prime(n):
    if n == 2:
        return 3
    if not is_prime(n):
        raise ValueError(f'{n} is not a prime')

    isPrime = False
    next = n + 2
    while not isPrime:
        isPrime = is_prime(next)
        next = next if isPrime else next + 2
    return next


def prime_factors(n):
    prime = 2 + (n & 1)
    factors = []
    while n > 1:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        prime = get_next_prime(prime)
        if n > 1 and is_prime(n):
            factors.append(n)
            break
    return factors