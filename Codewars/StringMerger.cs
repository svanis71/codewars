namespace Codewars
{
    public class StringMerger
    {
        public static bool isMerge(string merged, string s1, string s2)
        {
            if (s1.Length + s2.Length != merged.Length)
                return false;
            for (var i = 0; i < merged.Length; i++)
            {
                var longS1 = "";
                for (var j = i; merged.Substring(i, j) == s1.Substring(0, j); j++)
                    longS1 += s1.Substring(i, j);
                var longS2 = "";
                for (var j = i; merged.Substring(i, j) == s2.Substring(0, j); j++)
                    longS2 += s1.Substring(i, j);
                if (longS1.Length >= longS2.Length)
                    s1.Remove(0, longS1.Length);
                else
                    s2.Remove(0, longS2.Length);
            }
            return true;
        }
    }
}