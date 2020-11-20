using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Security.Policy;

namespace Codewars
{
    class Program
    {
        static string[] shadesOfGrey(int n)
        {
            var list = new List<string>(n);
            for (var i = 1; i <= n && i < 255; i++)
            {
              list.Add(string.Format("#{0:x6}", (i << 16) + (i << 8) + i ));  
            }
            return list.ToArray();
        }

        //static MyBigInt_v1 Fact(int n)
        //{
        //    if (n == 1)
        //        return new MyBigInt_v1(1);
        //    return new MyBigInt_v1(n) * Fact(n - 1);
        //}

        static int ReverseInt(int n)
        {
            var sn = n.ToString().ToCharArray();
            Array.Reverse(sn);
            return int.Parse(new string(sn));
        }

        static bool IsPalindrome(int n)
        {
            return n == ReverseInt(n);
        }

        public static int palindromeChainLength(int n)
        {
            var cnt = 0;
            var next = n;
            while (!IsPalindrome(next))
            {
                cnt++;
                next = next + ReverseInt(next);
            }
            return cnt;
        }

        static void Main(string[] args)
        {
            Console.WriteLine($"{palindromeChainLength(87)}");
            //foreach (var s in shadesOfGrey(1))
            //{
            //    Console.WriteLine(s);
            //}
            //Console.WriteLine($"5! = {Fact(5)}");
            //Console.WriteLine($"100! = {Fact(100)}");
            //var b1 = new MyBigInt_v1(123456);
            //var b2 = new MyBigInt_v1(7891);
            //var res = Fact(999);
            //var b1 = new MyBigInt_v1(1587);
            //var b2 = new MyBigInt_v1(599);
            //Console.WriteLine((b1+b2).ToString());
            Console.ReadKey();
        }
    }
}
