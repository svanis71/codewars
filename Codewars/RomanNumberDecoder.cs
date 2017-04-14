using System.Collections.Generic;

namespace Codewars
{
    public class RomanNumberDecoder
    {
        private static readonly Dictionary<char, int> _romanNumbers = new Dictionary<char, int>()
        {
            {'M', 1000},
            {'D', 500},
            {'C', 100},
            {'L', 50},
            {'X', 10},
            {'V', 5},
            {'I', 1}
        };

        public static int Decoder(string romanNumber)
        {
            var sum = 0;
            for(var i = 0; i < romanNumber.Length; i++)
            {
                if (i == romanNumber.Length - 1 || _romanNumbers[romanNumber[i]] >= _romanNumbers[romanNumber[i + 1]])
                    sum += _romanNumbers[romanNumber[i]];
                else
                {
                    sum += _romanNumbers[romanNumber[i + 1]] - _romanNumbers[romanNumber[i]];
                    i++;
                }
            }
            return sum;
        }
    }
}