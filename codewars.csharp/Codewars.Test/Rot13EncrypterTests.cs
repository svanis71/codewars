using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class Rot13EncrypterTests
    {
        [TestMethod]
        public void TestEmpty()
        {
            Assert.AreEqual(string.Empty, Rot13Encrypter.ROT135(""));
        }

        [TestMethod]
        public void TestOneLetter()
        {
            Assert.AreEqual("G", Rot13Encrypter.ROT135("T"));
        }

        [TestMethod]
        public void TestFox()
        {
            Assert.AreEqual("Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf", 
                Rot13Encrypter.ROT135("The quick brown fox jumps over the 2 lazy dogs"));
        }

    }
}
