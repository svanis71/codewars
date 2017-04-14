using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class PrimeDecompTest
    {

        [TestMethod]
        public void TestPrimeDecomp1()
        {
            Assert.AreEqual("(2**2)", PrimeDecomp.factors(4));
        }

        [TestMethod]
        public void TestPrimeDecomp2()
        {
            Assert.AreEqual("(2**3)(5)", PrimeDecomp.factors(40));
        }

        [TestMethod]
        public void TestPrimeDecomp3()
        {
            Assert.AreEqual("(2**5)(5)(7**2)(11)", PrimeDecomp.factors(86240));
        }

        [TestMethod]
        public void TestPrimeDecomp4()
        {
            Assert.AreEqual("(7919)", PrimeDecomp.factors(7919));
        }

        [TestMethod]
        public void TestPrimeDecomp5()
        {
            Assert.AreEqual("(3)(17**2)(31)(677)", PrimeDecomp.factors(18195729));
        }

        [TestMethod]
        public void TestPrimeDecomp6()
        {
            Assert.AreEqual("(2**2)(3**3)(5)(7)(11**2)(17)", PrimeDecomp.factors(7775460));
        }

        [TestMethod]
        public void TestPrimeDecomp7()
        {
            Assert.AreEqual("(2**4)(3)(11)(43)(15073)", PrimeDecomp.factors(342217392));
        }
    }
}
