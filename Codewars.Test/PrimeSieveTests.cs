using System;
using Codewars.Numbers;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class PrimeSieveTests
    {
        [TestMethod]
        public void Test1Prime()
        {
            int[] primes = PrimeNumbers.GenerateWithSundaram(1);
            Assert.AreEqual(1, primes.Length);
            Assert.AreEqual(2, primes[0]);
        }

        [TestMethod]
        public void Test2Prime()
        {
            int[] primes = PrimeNumbers.GenerateWithSundaram(10);
            Assert.AreEqual(4, primes.Length);
            Assert.AreEqual(3, primes[1]);
        }

        [TestMethod]
        public void Test3Prime()
        {
            int[] primes = PrimeNumbers.GenerateWithSundaram(100);
            int[] expected = PrimeNumbers.GeneratePrimesBruteForce(100);
            Assert.AreEqual(expected.Length, primes.Length);
        }

    }
}
