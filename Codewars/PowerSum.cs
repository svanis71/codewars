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
                    n--;
                }
            }
            return num - 1;
        }

        public static bool IsPowerSum(long n)
        {
            var exp = 1;
            var k = n;
            var sum = 0L;
            var cnt = 0;
            while (k > 0)
            {
                sum += (k % 10);
                k /= 10;
            }
            if (sum > 1)
            {
                while (n % sum == 0)
                    n /= sum;
                return n == 1;
            }
            return false;
        }
    }
}
