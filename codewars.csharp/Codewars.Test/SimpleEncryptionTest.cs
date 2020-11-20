using System;
using System.Runtime.CompilerServices;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class SimpleEncryptionTest
    {
        private const string Indata = "This is a test!";

        [TestMethod]
        public void TestEncryptNull()
        {
            Assert.IsNull(Kata.Encrypt(null, 1));
        }

        [TestMethod]
        public void TestEncryptEmpty()
        {
            Assert.AreEqual(string.Empty, Kata.Encrypt(string.Empty, 1));
        }

        [TestMethod]
        public void TestEncryptNZero()
        {
            Assert.AreEqual(Indata, Kata.Encrypt(Indata, 0));
        }

        [TestMethod]
        public void TestEncryptNLessOrEqualToZero()
        {
            Assert.AreEqual(Indata, Kata.Encrypt(Indata, -1));
        }

        [TestMethod]
        public void TestEncryptNOne()
        {
            Assert.AreEqual("hsi  etTi sats!", Kata.Encrypt(Indata, 1));
        }

        [TestMethod]
        public void TestEncryptNTwo()
        {
            Assert.AreEqual("s eT ashi tist!", Kata.Encrypt(Indata, 2));
        }

        [TestMethod]
        public void TestEncryptNThree()
        {
            Assert.AreEqual(" Tah itse sits!", Kata.Encrypt(Indata, 3));
        }

        [TestMethod]
        public void TestEncryptNFour()
        {
            Assert.AreEqual(Indata, Kata.Encrypt(Indata, 4));
        }

        [TestMethod]
        public void TestDecryptEmpty()
        {
            Assert.AreEqual(string.Empty, Kata.Decrypt(string.Empty, 42));
        }

        [TestMethod]
        public void TestDecryptNull()
        {
            Assert.IsNull(Kata.Decrypt(null, 42));
        }

        [TestMethod]
        public void TestDecryptNZero()
        {
            Assert.AreEqual(Indata, Kata.Decrypt(Indata, 0));
        }

        [TestMethod]
        public void TestDecryptNOne()
        {
            Assert.AreEqual("This is a test!", Kata.Decrypt("hsi  etTi sats!", 1));
        }

        [TestMethod]
        public void TestDecryptNTwo()
        {
            Assert.AreEqual("This is a test!", Kata.Decrypt("s eT ashi tist!", 2));
        }

        [TestMethod]
        public void TestDecryptNThree()
        {
            Assert.AreEqual("This is a test!", Kata.Decrypt(" Tah itse sits!", 3));
        }

        [TestMethod]
        public void TestDecryptNFour()
        {
            Assert.AreEqual("This is a test!", Kata.Decrypt("This is a test!", 4));
        }

    }

}
