using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Codewars
{
    public class RomanNumberEncoder
    {
        private Dictionary<int, string> roman = new Dictionary<int, string>()
        {
            {1000, "M"},
            {500, "D"},
            {100, "C"},
            {50, "L"},
            {10, "X"},
            {5, "V"},
            {1, "I"},
            {0, ""}
        };

        public string Encode(int number)
        {
            if (number == 0)
                return "";

            var rom = new StringBuilder();

            int tmp = number;
            int next;
            var c = 1;
            for (; tmp > 10; c *= 10)
                tmp /= 10;
            if (tmp == 4 || tmp == 9)
            {
                tmp *= c;
                var d2 = roman.Keys.Where(p => p > tmp).Min();
                var d1 = d2 - tmp;
                rom.Append(roman[d1]);
                rom.Append(roman[d2]);
                next = number - tmp;
            }
            else
            {
                var d1 = roman.Keys.Where(p => p <= number).Max();
                int l = number / d1;
                next = number % d1;
                for (var i = 0; i < l; i++)
                {
                    rom.Insert(0, roman[d1]);
                }
            }
            return rom + Encode(next);
        }
    }
}
