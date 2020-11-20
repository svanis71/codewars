using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Codewars
{
    public static class Kata
    {
        public static string Encrypt(string text, int n)
        {
            var doNothing = string.IsNullOrEmpty(text) || n <= 0;
            if(doNothing)
                return text;
            var inLen = text.Length;
            var even = string.Empty;
            var odd = string.Empty;
            for (var i = 0; i < inLen; i += 2)
            {
                even += text[i];
                if (i + 1 < inLen)
<FÅ                {
                    odd += text[i + 1];
                }
            }
            return Encrypt(odd + even, n-1);
        }

        public static string Decrypt(string encryptedText, int n)
        {
            var doNothing = string.IsNullOrEmpty(encryptedText) || n <= 0;
            if (doNothing)
                return encryptedText;
            var decryptedText = string.Empty;
            var evens = encryptedText.Substring(0, encryptedText.Length / 2);
            var odds = encryptedText.Substring(evens.Length);
            for (var i = 0; i < odds.Length; i++)
            {
                decryptedText += odds[i];
                if (i < evens.Length)
                    decryptedText += evens[i];
            }
            return Decrypt(decryptedText, n - 1);
        }
    }
}

//  1234567
// 1234
// 567

//  12345678
// 1234
// 5678


// hsi  et
// Ti sats!

