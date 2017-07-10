using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class StrringMergerTests
    {
        [TestMethod]
        public void StringMergerTrue1()
        {
            Assert.IsTrue(StringMerger.isMerge("codewars", "code", "wars"), "codewars can be created from code and wars");
        }

        //[TestMethod]
        //public void StringMergerTrue2()
        //{
        //    Assert.IsTrue(StringMerger.isMerge("codewars", "cdwr", "oeas"), "codewars can be created from cdwr and oeas");
        //}

        //[TestMethod]
        //public void StringMergerFalse1()
        //{
        //    Assert.IsFalse(StringMerger.isMerge("codewars", "cod", "wars"), "Codewars are not codwars");
        //}

        // 'Bananas from Bahamas', 'Bahas', 'Bananas from am'
    }
}
