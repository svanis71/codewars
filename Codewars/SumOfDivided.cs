using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Codewars.Numbers;

namespace Codewars
{
    public class SumOfDivided
    {
        public static string sumOfDivided(int[] lst)
        {
            var copy = lst.Select(Math.Abs).OrderByDescending(p=>p).Select(p=>p).ToList();
            var primes = PrimeNumbers.GeneratePrimesBruteForce(copy.First());
            var result =new StringBuilder();
            foreach (var prime in primes)
            {
                if (lst.Any(p => p % prime == 0))
                {
                    var sum = lst.Where(p => p % prime == 0).Sum();
                    result.AppendFormat("({0} {1})", prime, sum);
                }
            }
            return result.ToString();
        }
    }
}
