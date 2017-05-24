using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Codewars
{
    public class KPrimes
    {
        private static bool IsPrime(long n)
        {
            if ((n & 1) == 0)
                return n == 2;
            for (var i = 3; i * i <= n; i += 2)
            {
                if ((n % i) == 0)
                    return false;
            }
            return n != 1;
        }

        private static long GetNextPrime(long start, List<long> primeList)
        {
            var n = start + 1L + (start & 1L);
            if (primeList.Any(p => p >= n))
            {
                return primeList.Where(p => p >= n).Min(p => p);
            }
            var found = false;
            while (!found)
            {
                found = IsPrime(n);
                if (!found)
                    n += 2;
            }
            primeList.Add(n);
            return n;
        }

        public static long[] CountKprimes(int k, long start, long end)
        {
            var list = new List<long>();
            var primeList = new List<long>();
            var loopCount = 0L;
            for (var i = start; i <= end; i++)
            {
                var cnt = 0;
                var div = i;
                var done = false;

                for (var prime = 2L; div > 0 && !done; prime = GetNextPrime(prime, primeList))
                {
                    var isPrime = false;
                    while (true)
                    {
                        loopCount++;
                        isPrime = IsPrime(div);
                        if (div % prime != 0 || isPrime)
                            break;
                        div /= prime;
                        cnt++;
                    }
                    if (isPrime || div == 1)
                    {
                        done = true;
                        cnt++;
                    }
                }

                if (cnt == k)
                    list.Add(i);
            }
            Trace.WriteLine($"Loop count is {loopCount}");
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
