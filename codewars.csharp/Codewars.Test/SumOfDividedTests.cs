using System;
using System.Diagnostics;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class SumOfDividedTests
    {
        [TestMethod]
        public void TestSumDivided1()
        {
            var lst = new[] { 12, 15 };
            Assert.AreEqual("(2 12)(3 27)(5 15)", SumOfDivided.sumOfDivided(lst));
        }

        [TestMethod]
        public void TestSumDivided2()
        {
            var lst = new int[] {15, 21, 24, 30, 45,};
            Assert.AreEqual("(2 54)(3 135)(5 90)(7 21)", SumOfDivided.sumOfDivided(lst));
        }

        [TestMethod]
        public void TestSumDivided3()
        {
            var lst = new int[] { 114, 237, 421 };
            Assert.AreEqual("(2 114)(3 351)(19 114)(79 237)(421 421)", SumOfDivided.sumOfDivided(lst));
        }
    }
}
