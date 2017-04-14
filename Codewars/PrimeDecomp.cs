using System.Linq;
using System.Text;
using Codewars.Numbers;

namespace Codewars
{
    public class PrimeDecomp
    {
        public static string factors(int n)
        {
            var primes = PrimeNumbers.GeneratePrimesBruteForce(n / 2 + 1);//.OrderByDescending(p=>p).ToArray();
            if (n.IsPrime())
                return $"({n})";
            var res = new StringBuilder();
            foreach (var prime in primes)
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
            }
            return res.ToString();
        }
    }
}
