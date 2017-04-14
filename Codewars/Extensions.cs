using System;
using  System.Linq;

namespace Codewars
{
    public static class Extensions
    {
        public static int ToInt(this char c)
        {
            return (int) (c - '0');
        }

        public static char ToChar(this int dig)
        {
            return (char) (dig + '0');
        }

        public static int FindEvenIndex(this int[] arr)
        {
            var findex = -1;
            var rev = arr.Reverse().ToArray();
            for (var i = 1; i < arr.Length; i++)
            {
                var sum = arr.Take(i).Aggregate((p, c) => p + c);
                var rnum = arr.Length - i - 1; 
                var revTot = rnum > 0 ? rev.Take(rnum).Aggregate((p, c) => p + c) : sum + 1;
                if (sum == revTot)
                    findex = i;
            }
            return findex;
        }

    }
}