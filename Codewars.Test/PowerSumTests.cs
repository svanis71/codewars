using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class PowerSumTests
    {
        [TestMethod]
        public void TestPowerSum1()
        {
            Assert.AreEqual(81, PowerSumDig.PowerSumDigTerm(1));
        }

        [TestMethod]
        public void TestPowerSum2()
        {
            Assert.AreEqual(512, PowerSumDig.PowerSumDigTerm(2));
        }

        [TestMethod]
        public void TestPowerSum3()
        {
            Assert.AreEqual(2401, PowerSumDig.PowerSumDigTerm(3));
        }

        [TestMethod]
        public void TestPowerSum4()
        {
            Assert.AreEqual(4913, PowerSumDig.PowerSumDigTerm(4));
        }

        [TestMethod]
        public void TestPowerSum5()
        {
            Assert.AreEqual(5832, PowerSumDig.PowerSumDigTerm(5));
        }

        [TestMethod]
        public void TestPowerSum6()
        {
            for (var i = 1; i < 16; i++)
            {
                var t1 = new TimeSpan(DateTime.Now.Ticks);
                Console.WriteLine($"PowerSum {i} is {PowerSumDig.PowerSumDigTerm(i)}");
                var t2 = new TimeSpan(DateTime.Now.Ticks);
                Console.WriteLine($"Time was {(t2-t1).Duration()}");
            }
        }

        //[TestMethod]
        //public void TestPowerSum15()
        //{
        //    Assert.AreEqual(60466176, PowerSumDig.PowerSumDigTerm(15));
        //}

    }
}