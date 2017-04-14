using System;
using System.Linq;

namespace Codewars
{
    public class Rot13Encrypter
    {
        private static char Rotate(char ch)
        {
            if (char.IsNumber(ch))
                return ch < '5' ? (char) (ch + 5) : (char) (ch - 5);  
            if(char.IsLetter(ch))
                return char.ToUpper(ch) < 'N' ? (char) (ch + 13) : (char) (ch - 13);
            return ch;
        }
        public static string ROT135(string input)
        {
            return new string(input.ToCharArray().Select(p => Rotate(p)).ToArray());
        }
    }
}
