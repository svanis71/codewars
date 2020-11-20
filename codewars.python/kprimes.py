from utils import prime_factors, generate_primes_to


def is_kprime(k, n):
    return len(prime_factors(n)) == k


def kprimes(k, start, end):
    return [i for i in range(start, end + 1) if is_kprime(k, i)]

def puzzle(n):
    kp1 = generate_primes_to(n)
    kp3 = kprimes(3, 0, n)
    kp7 = kprimes(7, 0, n)
    return sum([sum([len([p7 for p7 in kp7 if (p1 + p3 + p7) == n]) for p3 in kp3]) for p1 in kp1])

def consec_kprimes(k, a):
    b = a[1:]
    cnt = 0
    for n1,n2 in zip(a,b):
        if is_kprime(k, n1) and is_kprime(k, n2):
           cnt += 1
    return cnt

