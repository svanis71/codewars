import unittest

from utils import is_prime, generate_primes_to, get_next_prime, prime_factors


class PrimesTests(unittest.TestCase):
    def test_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 43, 83]
        for p in primes:
            self.assertTrue(is_prime(p), f'Testar {p}')

    def test_generate_to(self):
        self.assertEqual(303, len(generate_primes_to(2000)), "Generate primes upto 2000")

    def test_next_prime(self):
        tests = [(3, 2), (11, 7), (83, 79), (509, 503)]
        for (n, c) in tests:
            self.assertEqual(n, get_next_prime(c), f'get_next_prime({c}) should be {n}')

    def test_next_prime_no_prime(self):
        with self.assertRaises(ValueError):
            get_next_prime(4)

    def test_prime_factors_8(self):
        self.assertEqual([2, 2, 2], prime_factors(8))

    def test_prime_factors_30(self):
        self.assertEqual([2, 3, 5], prime_factors(30))


if __name__ == '__main__':
    unittest.main()
