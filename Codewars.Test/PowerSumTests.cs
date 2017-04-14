using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class PowerSumTests
    {
        [TestMethod]
        public void TestMethod1()
        {
            Assert.AreEqual(81, PowerSumDig.PowerSumDigTerm(1));
        }

        [TestMethod]
        public void TestMethod2()
        {
            Assert.AreEqual(512, PowerSumDig.PowerSumDigTerm(2));
        }

        [TestMethod]
        public void TestMethod3()
        {
            Assert.AreEqual(2401, PowerSumDig.PowerSumDigTerm(3));
        }

        [TestMethod]
        public void TestMethod4()
        {
            Assert.AreEqual(4913, PowerSumDig.PowerSumDigTerm(4));
        }

        //[TestMethod]
        //public void TestMethod5()
        //{
        //    Assert.AreEqual(4913, PowerSumDig.PowerSumDigTerm(15));
        //}

    }
}