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
    }
}
