using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.Test
{
    [TestClass]
    public class MagnetsTest
    {

        private static Random rnd = new Random();
        private static void assertFuzzyEquals(double act, double exp)
        {
            bool inrange = Math.Abs(act - exp) <= 1e-6;
            if (inrange == false)
            {
                string specifier = "#0.000000";
                Console.WriteLine(
                    "At 1e-6: Expected must be " + exp.ToString(specifier) + ", but got " + act.ToString(specifier));
            }
            Assert.AreEqual(true, inrange);
        }

        [TestMethod]
        public void MagnetTest1()
        {
            Console.WriteLine("Fixed Tests: Doubles");
            assertFuzzyEquals(Magnets.Doubles(1, 10), 0.5580321939764581); // 0.5580321939764581
        }
    }
}
