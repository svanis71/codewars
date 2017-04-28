using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars
{
    public class YpkCalculator
    {
        public Dictionary<double, bool> drive(double[,] drinks, string finished, string drive_time)
        {
            var totalDrinks = 0.0;
            for (var i = 0; i < drinks.GetLength(0); i++)
            {
                totalDrinks += drinks[i, 0] * drinks[i, 1] / 1000;
            }
            var startTime = finished.Split(':').Select(int.Parse).ToArray();
            var driveTime = drive_time.Split(':').Select(int.Parse).ToArray();
            var t1 = DateTime.Today.Add(new TimeSpan(startTime[0], startTime[1], 0));
            var t2 = DateTime.Today.Add(new TimeSpan(driveTime[0], driveTime[1], 0));
            if (t2 < t1)
                t2 = t2.AddDays(1);
            var diff = (t2 - t1).TotalMinutes / 60.0;
            var x = diff - totalDrinks;
            Console.WriteLine($"diff = {diff}, total={totalDrinks}, test = {x > 0}");
            return new Dictionary<double, bool> { { Math.Round(totalDrinks, 2), x > 0 } };
        }
    }
}
