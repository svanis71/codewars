
using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Net.NetworkInformation;
using System.Runtime.CompilerServices;
using System.Text;

namespace Codewars
{
    public class MyBigInt
    {
        private readonly List<byte> _value = new List<byte>();
        public int DataLength => _value.Count;

        public MyBigInt(int intValue)
        {
            var t = intValue;
            while (t != 0)
            {
                var b = (byte)(t & 0xff);
                _value.Insert(0, (byte)(b-'0'));
                t = t >> 8;
            }
        }

        public MyBigInt()
        {
            _value.Add((byte)0);
        }

        public MyBigInt(string newVal)
        {
            foreach(var c in newVal)
                _value.Insert(0, (byte)(c-'0'));
        }

        private static string Add(string s1, string s2)
        {
            var sum = "";
            var carry = 0;
            s1 = s1.PadLeft(s2.Length, '0');
            for (var i = s1.Length - 1; i >= 0; i--)
            {
                var t = carry + s1[i].ToInt() + s2[i].ToInt();
                carry = t / 10;
                t = t % 10;
                sum = t.ToChar() + sum;
            }
            if (carry != 0)
                sum = carry + sum;
            return sum;
        }

        public static MyBigInt operator +(MyBigInt bi1, MyBigInt bi2)
        {
            var carry = 0;
            var len1 = bi1.DataLength;
            var len2 = bi2.DataLength;
            var result = new MyBigInt();
        
            while (len1 > 0 && len2 > 0)
            {
                var i1 = len1 >= 0 ? bi1.GetByte(len1) : 0;
                var i2 = len2 >= 0 ? bi1.GetByte(len2) : 0;
                var dig = i1 + i2 + carry;
                carry = dig >> 8;
                dig = dig & 0xff;
                result.InsertByte((byte)dig);
                len1--;
                len2--;
            }
            if(carry > 0)
                result.InsertByte((byte)carry);
            return result;
//            return new MyBigInt(Add(n1.ToString(), n2.ToString()));
        }

        //public MyBigInt MultiplyBy(MyBigInt bi2)
        //{
        //    var over = _value;
        //    var under = bi2.ToString();
        //    var tail = "";
        //    int p = under.Length - 1;
        //    bool foundTail = false;
        //    var foo = int.Parse(this.ToString());
        //    if(foo % 50 == 0)
        //        Console.WriteLine($"Nu har vi kört {foo} varv...");
        //    while (p >= 0 && under[p] == '0')
        //    {
        //        foundTail = true;
        //        p--;
        //    }
        //    if (foundTail)
        //    {
        //        tail = under.Substring(p + 1);
        //        under = under.Substring(0, p+1);
        //    }

        //    List<string> rows = new List<string>();
        //    var zeros = "";
        //    for (int i = under.Length - 1; i >= 0; i--)
        //    {
        //        var digit = (int)(under[i] - '0');
        //        List<char> row = new List<char>();
        //        var carry = 0;
        //        for (int j = over.Length - 1; j >= 0; j--)
        //        {
        //            var other = (int)(over[j] - '0');
        //            var t = carry + digit * other;
        //            carry = t / 10;
        //            t = t % 10;
        //            row.Insert(0, (char)(t + '0'));
        //        }
        //        if (carry > 0)
        //            row.Insert(0, (char)(carry + '0'));
        //        row.AddRange(zeros);
        //        zeros = zeros + "0";
        //        rows.Add(new string(row.ToArray()));
        //    }

        //    var sum = rows[0];
        //    for (var r = 1; r < rows.Count; r++)
        //    {
        //        sum = Add(sum, rows[r]);
        //    }
        //    sum += tail;
        //    return new MyBigInt(sum);
        //}

        //public static MyBigInt operator *(MyBigInt n1, MyBigInt n2)
        //{
        //    return n1.MultiplyBy(n2);
        //}

        //public static bool operator !=(MyBigInt n1, MyBigInt n2)
        //{
        //    return n1.ToString() != n2.ToString();
        //}

        //public static bool operator ==(MyBigInt n1, MyBigInt n2)
        //{
        //    return n1.ToString() == n2.ToString();
        //}

        public byte GetByte(int index)
        {
            return _value[index];
        }

        public void InsertByte(byte bytVal)
        {
            _value.Insert(0, bytVal);
        }
        public override string ToString()
        {
            var sb = new StringBuilder();
            foreach (var b in _value)
            {
                sb.Append((char)(b+'0'));
            }
            return sb.ToString();
        }
    }
}