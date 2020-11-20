using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class BraceTest
    {
        [TestMethod]
        public void TestBrace1()
        {
            Assert.IsTrue(Brace.validBraces("([{}])"));
        }

        [TestMethod]
        public void TestBrace2()
        {
            Assert.IsFalse(Brace.validBraces("([{(})])"));
        }

    }
}
