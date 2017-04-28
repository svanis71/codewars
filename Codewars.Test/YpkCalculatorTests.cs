using System;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class YpkCalculatorTests
    {
        //[TestMethod]
        public void ExampleTest1()
        {
            var test = new YpkCalculator();
            double[,] alcohol = new double[,] { { 5.2, 568.0 }, { 12.0, 175.0 } };
            Dictionary<double, bool> solution = test.drive(alcohol, "16:00", "01:00");
            Dictionary<double, bool> result = new Dictionary<double, bool> { { 5.05, true } };
            Assert.AreEqual(result, solution, "Expected : { 5.05, true }");
        }
        //[TestMethod]
        public void ExampleTest2()
        {
            var test = new YpkCalculator();
            double[,] alcohol = new double[,] { { 5.2, 568.0 }, { 5.2, 568.0 }, { 5.2, 568.0 }, { 12.0, 175.0 }, { 12.0, 175.0 }, { 12.0, 175.0 } };
            Dictionary<double, bool> solution = test.drive(alcohol, "23:00", "08:15");
            Dictionary<double, bool> result = new Dictionary<double, bool> { { 15.16, false } };
            Assert.AreEqual(result, solution, "Expected : { 15.16, false }");
        }
        //[TestMethod]
        public void ExampleTest3()
        {
            var test = new YpkCalculator();
            double[,] alcohol = new double[,] { { 15.5, 568.0 } };
            Dictionary<double, bool> solution = test.drive(alcohol, "23:00", "06:45");
            Dictionary<double, bool> result = new Dictionary<double, bool> { { 8.8, false } };
            Assert.AreEqual(result, solution, "Expected : { 8.8, false }");
        }
        //[TestMethod]
        public void ExampleTest4()
        {
            var test = new YpkCalculator();
            double[,] alcohol = new double[,] { { 10.0, 100.0 } };
            Dictionary<double, bool> solution = test.drive(alcohol, "20:00", "21:00");
            Dictionary<double, bool> result = new Dictionary<double, bool> { { 1.0, false } };
            Assert.AreEqual(result, solution, "Expected : { 1.0, false }");
        }
        //[TestMethod]
        public void ExampleTest5()
        {
            var test = new YpkCalculator();
            double[,] alcohol = new double[,] { { 10.0, 100.0 } };
            Dictionary<double, bool> solution = test.drive(alcohol, "20:00", "21:01");
            Dictionary<double, bool> result = new Dictionary<double, bool> { { 1.0, true } };
            Assert.AreEqual(result, solution, "Expected : { 1.0, true }");
        }
    }
}
