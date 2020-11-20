using System;

namespace Codewars
{
    public class Brace
    {
        public static bool validBraces(String braces)
        {
            var valid = true;
            while (valid && braces.Length > 0)
            {
                var idx = braces.IndexOf("()");
                idx = idx > -1 ? idx : braces.IndexOf("[]");
                idx = idx > -1 ? idx : braces.IndexOf("{}");
                if (idx > -1)
                {
                    braces = braces.Remove(idx, 2);
                }
                else
                    valid = false;
            }

            return valid;
        }
    }
}
