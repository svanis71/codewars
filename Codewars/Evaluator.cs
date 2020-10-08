using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Codewars
{
    public class Evaluator
    {
        public static double Evaluate(string expression)
        {
            var parts = Regex.Split(expression, @"[*/+-]");

            foreach (var op in parts)
            {
                
            }
            return 0.0;
        }
    }
}
