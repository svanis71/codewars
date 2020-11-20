using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Codewars
{
    public class PowerSumDig
    {
        public static long PowerSumDigTerm(int n)
        {
            var l = new List<long>();
            for (var i = 2L; i < 100; i++)
            {
                for(var v = i*i; v > 0 && v < long.MaxValue; v *= i)
                { 
                    if (DigitSum(v) == i)
                        l.Add(v);
                }
            }
            l.Sort();
            return l[n-1];
        }

        private static long DigitSum(long n)
        {
            var sum = 0L;
            while (n > 0)
            {
                sum += (n % 10);
                n /= 10;
            }
            return sum;
        }
    }
}
