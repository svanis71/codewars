using System.Dynamic;
using System.Linq;
using System.Text;
using Codewars.Numbers;

namespace Codewars
{
    public class PrimeDecomp
    {
        public static string factors(int n)
        {
            if (n.IsPrime())
                return $"({n})";
            var res = new StringBuilder();
            var prime = 2;
            while(n > 1)
            {
                var cnt = 0;
                while (n % prime == 0)
                {
                    cnt++;
                    n /= prime;
                }
                if (cnt > 0)
                {
                    if (cnt > 1)
                        res.Append($"({prime}**{cnt})");
                    else
                        res.Append($"({prime})");
                }
                prime = prime.GetNextPrime();
            }
            return res.ToString();
        }
    }
}
