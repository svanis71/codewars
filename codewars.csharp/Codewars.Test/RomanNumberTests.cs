using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class RomanNumberTests
    {
        private readonly RomanNumberEncoder _encoder = new RomanNumberEncoder();

        [TestMethod]
        public void TestOne()
        {
            Assert.AreEqual("I", _encoder.Encode(1));
        }

        [TestMethod]
        public void TestTwo()
        {
            Assert.AreEqual("II", _encoder.Encode(2));
        }

        [TestMethod]
        public void TestThree()
        {
            Assert.AreEqual("III", _encoder.Encode(3));
        }

        [TestMethod]
        public void TestFour()
        {
            Assert.AreEqual("IV", _encoder.Encode(4));
        }

        [TestMethod]
        public void TestThirty()
        {
            Assert.AreEqual("XXX", _encoder.Encode(30));
        }

        [TestMethod]
        public void TestSeventy()
        {
            Assert.AreEqual("LXX", _encoder.Encode(70));
        }
 
        [TestMethod]
        public void Test1666()
        {
            Assert.AreEqual("MDCLXVI", _encoder.Encode(1666));
        }

        [TestMethod]
        public void Test1984()
        {
            Assert.AreEqual("MCMLXXXIV", _encoder.Encode(1984));
        }

        [TestMethod]
        public void Test2017()
        {
            Assert.AreEqual("MMXVII", _encoder.Encode(2017));
        }

        // Decode
        [TestMethod]
        public void TestI()
        {
            Assert.AreEqual(1, RomanNumberDecoder.Decoder("I"));
        }

        [TestMethod]
        public void TestII()
        {
            Assert.AreEqual(2, RomanNumberDecoder.Decoder("II"));
        }

        [TestMethod]
        public void TestIII()
        {
            Assert.AreEqual(3, RomanNumberDecoder.Decoder("III"));
        }

        [TestMethod]
        public void TestIV()
        {
            Assert.AreEqual(4, RomanNumberDecoder.Decoder("IV"));
        }

        [TestMethod]
        public void TestV()
        {
            Assert.AreEqual(5, RomanNumberDecoder.Decoder("V"));
        }

        [TestMethod]
        public void TestDecodeMDCLXVI()
        {
            Assert.AreEqual(1666, RomanNumberDecoder.Decoder("MDCLXVI"));
        }

        [TestMethod]
        public void TestDecodeMCMLXXXIV()
        {
            Assert.AreEqual(1984, RomanNumberDecoder.Decoder("MCMLXXXIV"));
        }

    }
}
