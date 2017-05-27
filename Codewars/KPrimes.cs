using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Codewars
{
    public class KPrimes
    {
        public static bool IsPrime(long n)
        {
            if (n <= 1)
                return false;
            if (n % 2 == 0 || n % 3 == 0)
                return n == 2;
            for (var i = 5; i * i <= n; i += 6)
            {
                if (n % i == 0 || n % (i+2) == 0)
                    return false;
            }
            return true;
        }

        static long GetNextPrime(long n)
        {
            if (n == 2)
                return 3;
            var isPrime = false;
            var next = n + 2;
            while (!isPrime)
            {
                isPrime = IsPrime(next);
                next = isPrime ? next : next + 2;
            }
            return next;
        }

        public static int factors(long n, int max)
        {
            var prime = 2 + (n & 1);
            var cnt = 0;
            var testIfPrime = true;
            while (n > 1)
            {
                if (testIfPrime)
                {
                    if (IsPrime(n))
                        return cnt + 1;
                    testIfPrime = false;
                }
                while (n % prime == 0 && cnt <= max)
                {
                    cnt++;
                    n /= prime;
                    testIfPrime = true;
                }
                if (cnt <= max && n > 1)
                    prime = GetNextPrime(prime);
                else if(cnt > max)
                    return cnt + 1;
            }
            return cnt;
        }
        public static long[] CountKprimes(int k, long start, long end)
        {
            Console.WriteLine($"Find {k}-primes from {start} to {end}");
            var list = new List<long>();
            var primeList = new List<long>() {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
            for (var i = start; i <= end; i++)
            {
                if (factors(i, k) == k)
                    list.Add(i);
            }
            return list.ToArray();
        }

        public static int Puzzle(int i)
        {
            var kprimes1 = CountKprimes(1, 0, i);
            var kprimes3 = CountKprimes(3, 0, i);
            var kprimes7 = CountKprimes(7, 0, i);

            return kprimes1.Sum(p1 => kprimes3.Sum(p3 => kprimes7.Count(p7 => (p1 + p3 + p7) == i)));
        }
    }
}
