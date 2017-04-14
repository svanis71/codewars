using System;
using System.Collections;
using System.Collections.Generic;

namespace Codewars.Numbers
{
    public static class PrimeNumbers
    {
        public static bool IsPrime(this int n)
        {
            if ((n & 1) == 0)
                return n == 2;
            for (var i = 3; i*i <= n; i += 2)
            {
                if ((n % i) == 0)
                    return false;
            }
            return n != 1;
        }

        public static int[] GeneratePrimesBruteForce(int max)
        {
            var primes = new List<int>() {2};
            for (var i = 3; i <= max; i += 2)
            {
                if (i.IsPrime())
                    primes.Add(i);
            }
            return primes.ToArray();
        }

        public static int[] GenerateWithSundaram(int n)
        {
            var k = n / 2;
            var candidates = new BitArray(k + 1);
            candidates.SetAll(true);

            for (var i = 1; i < k; i++)
            {
                var denominator = (i << 1) + 1;
                var maxVal = (k - i) / denominator;
                for (int j = i; j <= maxVal; j++)
                {
                    candidates[i + j * denominator] = false;
                }
            }

            var primes = new List<int>() {2};
            for (var i = 1; i < k; i++)
            {
                if (candidates[i])
                {
                    primes.Add((i << 1) + 1);
                }
            }

            return primes.ToArray();
        }
    }
}