using System;
using System.Diagnostics;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class KPrimeTests
    {
        private string Array2String(long[] list)
        {
            return "[" + string.Join(", ", list) + "]";
        }
        private void RunTest(string actual, string expected)
        {
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void KPrimesTest0()
        {
            RunTest(Array2String(KPrimes.CountKprimes(3, 10, 20)),
                Array2String(new long[]
                    {12, 18, 20}));
        }

        [TestMethod]
        public void KPrimesTest1()
        {
            RunTest(Array2String(KPrimes.CountKprimes(5, 500, 600)),
                Array2String(new long[]
                    {500, 520, 552, 567, 588, 592, 594}));
        }

        [TestMethod]
        public void KPrimesTest2()
        {
            // 4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95
            // 4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95
            RunTest(Array2String(KPrimes.CountKprimes(2, 0, 100)),
                Array2String(new long[]
                {4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51,
                    55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95}));
        }

        [TestMethod]
        public void KPrimesTest3()
        {
            RunTest(Array2String(KPrimes.CountKprimes(3, 0, 100)),
                Array2String(new long[]
                {8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76,
                    78, 92, 98, 99}));
        }

        [TestMethod]
        public void KPrimesTest4()
        {
            RunTest(Array2String(KPrimes.CountKprimes(5, 1000, 1100)),
                Array2String(new long[]
                    {1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100}));
        }

        [TestMethod]
        public void KPrimeTest5()
        {
            // k=2 start=5407774 end=5410400
            Trace.WriteLine(Array2String(KPrimes.CountKprimes(8, 10000000, 10000200)));
        }

        [TestMethod]
        public void KPrimesTest6()
        {
            // Find 4-primes from 3975825 to 3977469        
            Console.WriteLine(Array2String(KPrimes.CountKprimes(4, 3975825, 3977469)));
        }

        [TestMethod]
        public void KPrimesTest7()
        {
            // Find 6-primes from 5514238 to 5519031
            Console.WriteLine(Array2String(KPrimes.CountKprimes(6, 5514238, 5519031)));
        }

        [TestMethod]
        public void KPrimesTest8()
        {
            // Find 6-primes from 6635684 to 6639960
            Console.WriteLine(Array2String(KPrimes.CountKprimes(6, 6635684, 6639960)));
        }

        [TestMethod]
        public void KPrimesPuzzleTest1()
        {
            Assert.AreEqual(1, KPrimes.Puzzle(138));
        }

        [TestMethod]
        public void KPrimesPuzzleTest2()
        {
            Assert.AreEqual(2, KPrimes.Puzzle(143));
        }

        [TestMethod]
        public void KPrimesPuzzleTest3()
        {
            Assert.AreEqual(154, KPrimes.Puzzle(639));
        }
    }
}
