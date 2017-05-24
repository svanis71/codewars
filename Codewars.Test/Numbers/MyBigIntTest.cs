using System;
using Codewars.Numbers;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test.Numbers
{
    [TestClass]
    public class MyBigIntTest
    {
        [TestMethod]
        public void MyBigInt_Test_Plus1()
        {
            var b1 = new MyBigInt();
            var b2 = new MyBigInt();
            var b3 = b1 + b2;
            Assert.AreEqual("0", b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus2()
        {
            var b1 = new MyBigInt("1");
            var b2 = new MyBigInt("1");
            var b3 = b1 + b2;
            Assert.AreEqual("2", b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus3()
        {
            var b1 = new MyBigInt("7");
            var b2 = new MyBigInt("3");
            var b3 = b1 + b2;
            Assert.AreEqual("10", b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus4()
        {
            var b1 = new MyBigInt("12");
            var b2 = new MyBigInt("7");
            var b3 = b1 + b2;
            Assert.AreEqual("19", b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus5()
        {
            var b1 = new MyBigInt("10");
            var b2 = new MyBigInt("10");
            var b3 = b1 + b2;
            Assert.AreEqual("20", b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus6()
        {
            var b1 = new MyBigInt("1234");
            var b2 = new MyBigInt("1234567");
            var b3 = b1 + b2;
            Assert.AreEqual((1234+1234567).ToString(), b3.ToString());
        }

        [TestMethod]
        public void MyBigInt_Test_Plus7()
        {
            var b1 = new MyBigInt("1234567");
            var b2 = new MyBigInt("1234");
            var b3 = b1 + b2;
            Assert.AreEqual((1234567 + 1234).ToString(), b3.ToString());
        }

    }
}
