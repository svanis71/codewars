using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars
{
    public class Magnets
    {
        private static double Pow(int n, int p)
        {
            double sum = 1;
            for (var i = 0; i < p; i++)
            {
                sum *= n;
            }
            return sum;
        }

        private static double v(int k, int n)
        {
            return 1.0 / (k * Pow((n + 1), 2 * k));
        }

        private static double u(int k, int maxN)
        {
            var sum = 0.0;
            for (var n = 1; n <= maxN; n++)
            {
                sum += v(k, n);
            }
            return sum;
        }

        public static double Doubles(int maxk, int maxn)
        {
            var sumK = 0.0;
            for (var k = 1; k <= maxk; k++)
            {
                sumK += u(k, maxn);
            }
            return sumK;
        }
    }
}
