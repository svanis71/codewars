using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars.Numbers
{
    public class MyBigInt
    {
        private readonly string _value;

        public MyBigInt()
        {
            _value = "0";
        }

        public MyBigInt(string value)
        {
            _value = value;
        }

        public static MyBigInt operator +(MyBigInt n1, MyBigInt n2)
        {
            var pad = Math.Max(n1.ToString().Length, n2.ToString().Length);
            var s1 = n1.ToString().PadLeft(pad, '0').ToCharArray().Select(p=>p-'0').ToArray();
            var s2 = n2.ToString().PadLeft(pad, '0').ToCharArray().Select(p => p - '0').ToArray();
            var res = new StringBuilder();
            var carry = 0;
            for (var i = s1.Length - 1; i >= 0; i--)
            {
                var tmp = carry + s1[i] + s2[i];
                carry = tmp / 10;
                tmp = tmp % 10;
                res.Insert(0, tmp.ToString());
            }
            if(carry > 0)
                res.Insert(0, carry.ToString());
            return new MyBigInt(res.ToString());
        }

        public override string ToString()
        {
            return _value;
        }
    }
}
