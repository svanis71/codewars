using System;
using System.Text;

namespace Codewars.MiniStringFuck
{
    public class MyFirstInterpreter
    {
        private int _accumulator;
        private string _code;

        public MyFirstInterpreter(string code)
        {
            _code = code;
        }

        public string Interpret()
        {
            var outBuffer = new StringBuilder();
            foreach (var ch in _code.ToCharArray())
            {
                switch (ch)
                {
                    case '+':
                        _accumulator = (byte) ((_accumulator + 1) % 256);
                        break;
                    case '.':
                        outBuffer.Append(Convert.ToChar((byte)_accumulator));
                        break;
                }
            }
            return outBuffer.ToString();
        }
    }
}
