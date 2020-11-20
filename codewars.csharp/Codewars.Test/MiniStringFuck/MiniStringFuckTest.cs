using System;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Codewars.MiniStringFuck
{
    [TestClass]
    public class MiniStringFuckTest
    {
        [TestMethod]
        public void ShouldWorkForProgramsInÍnstruction()
        {
            RunTest("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++ +.++++++ +..++ +.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++ +.++++++++++++++++++++++++.++ +.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +.", "Hello, World!", "Should print Hello World");
            RunTest("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Should print english letters");
        }

        [TestMethod]
        public void shouldIgnoreAllNonCommandCharacters()
        {
            RunTest("+++++sdfs++++sdf++++sdklfjsdklfdjmvncxmnxmiuroewurwio+++++++++++++2423423++234+23++234+23++342+2++24++234++++++++++++++???++++++%+++++$#$#++++++++.+++++ssdf+++++++++++++++S+SDFSFSFWWET+BCV+BC+VBN+V+X+++.+++++++.WER.+++.++++++++++++++++++WERW+ERWE++++++++++++XCV+XC++++++++++++++++CXV+XC+XCV++++++++++++++++++++++++XCVXCXCVSTTYJFGDF++++++++++++++++s+dfs+sdf++sdsd+f++SDFS+DFS+FdfsdRTETRCBVCsdfsdf++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.",
                "Hello, World!", "Your interpreter should ignore all non-command characters");

            RunTest("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.\n   \t+.\n   \t+.\n   \t+.\n   \t+.\n   \t+.\n   \t+.\n   \t+.\n   \t+.\n   \t+.   \t\n+.   \t\n+.   \t\n+.   \t\n+.   \t\n+.   \t\n   \t+.\n+.\n+.\n+.\n+.\n+.\n+.\n+.\n+.\n+.\n+.",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Your interpreter should ignore all whitespace and newlines etc.");

            RunTest("+++,++<<-+-+-->>>-+++,++,++<+--+[>-+[--+]+<<<[+,,]+++]>+++,+,+++>>+++,++>[>>>>>]++++,+,+++[+++[+++[++]+++]++[++]--,,->><]+++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Your interpreter should not recognise any of \",\", \"-\", \"<\", \">\", \"[\", \"]\" (valid Brainfuck commands) as valid MiniStringFuck commands");

            RunTest("+++n+nnn*se++*e+e+***+enn+nn+***eess+++++s**+n++++++****+++s+s++*+ww++www+**+++++s**++++www***+w+w+www+****++++s+++++www+++s+++ss+ss+ws+s+.+w.s+s.+.+.ww+.s+.sw+ssssssw.+w.+.+s.+.+.+nessew.+.+.+.+.news+.+.+.+sewn.+.sesse+.+.see+.w",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Your interpreter should not recognise any of \"n\", \"e\", \"s\", \"w\", \"*\" (valid Paintfuck commands) as valid MiniStringFuck commands");
        }

        [TestMethod]
        public void shouldWorkForFixedTests()
        {
            RunTest(Adds(97) + Dots(26, "+"), "abcdefghijklmnopqrstuvwxyz");
            RunTest(Adds(67) + "." + Adds(44) + "." + Adds(245) + ".+." + Adds(18) + "." + Adds(234) + "." + Adds(17) + ".+.", "Codewars");
            RunTest(Adds(100) + "." + Adds(11) + "." + Adds(255) + "." + Adds(243) + "." + Adds(11) + "." + Adds(248) + "." + Adds(15) + "." + Adds(242) + "." + Adds(253) + "." + Adds(10) + "." + Adds(249) + "." + Adds(16) + "." + Adds(249) + "." + Adds(249) + ".", "donaldsebleung");
            RunTest(Adds(74) + "." + Adds(23) + "." + Adds(21) + "." + Adds(235) + ".", "Java");
            RunTest(Adds(69) + "." + Adds(46) + "." + Adds(252) + "." + Adds(253) + "." + Adds(245) + "." + Adds(13) + "." + Adds(249) + "." + Adds(12) + "." + Adds(173) + "." + Adds(82) + "." + Adds(253) + "." + Adds(244) + ".++++++++." + Adds(182) + "...", "Esolangs rock!!!");
        }

        [TestMethod]
        public void shouldWorkForRandomlyGeneratedMiniStringFuckPrograms()
        {
            for (var i = 0; i < 1; i++)
                TestRandomProgram();
        }

        private void RunTest(string code, string expected, string msg = "")
        {
            var interpreter = new MyFirstInterpreter(code);
            Assert.AreEqual(expected, interpreter.Interpret(), msg);
        }


        private void TestRandomProgram()
        {
            var code = CreateRandomProgram();
            var expected = Solution(code);
            RunTest(code, expected);
        }

        private static string Solution(string code)
        {
            var outBuffer = new StringBuilder();
            var accumulator = 0;
            foreach (var ch in code.ToCharArray())
            {
                if (ch == '+')
                    accumulator = ++accumulator % 256;
                else if (ch == '.')
                    outBuffer.Append(Convert.ToChar((byte) accumulator));
            }
            return outBuffer.ToString();
        }

        private static string Adds(int n)
        {
            return "+".PadRight(n, '+');
        }

        private static string Dots(int amount, string seperator)
        {
            return string.Join(seperator, Enumerable.Range(0, amount).Select(p => "."));
        }

        private static string CreateRandomProgram()
        {
            Random rnd = new Random();
            return string.Join("", Enumerable.Range(0, 1000 + (int)(rnd.NextDouble() * (9e3 + 1))).Select(p => rnd.NextDouble() < 0.9 ? "+" : "."));
//            return range(0, 1000 + (int)(Math.random() * (9e3 + 1))).mapToObj(i->(Math.random() < 0.9) ? "+" : ".").collect(joining());
        }
    }
}
