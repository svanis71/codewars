using System.Diagnostics;
using System.Linq;

namespace Codewars
{
    public class PowerSumDig
    {
        public static long PowerSumDigTerm(int n)
        {
            long num = 11;
            for (; n > 0; num++)
            {
                if (IsPowerSum(num))
                {
                    Trace.WriteLine($"Found {num}!");
                    n--;
                }
            }
            return num - 1;
        }

        private static bool IsPowerSum(long n)
        {
            var chars = n.ToString().ToCharArray();
            var sum = chars.Sum(ch => ch - '0');
            if (sum <= 1) return false;
            var prod = n;
            while (prod % sum == 0)
                prod /= sum;
            return prod == 1;
        }
    }
}
