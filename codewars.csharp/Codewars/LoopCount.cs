using System.Collections.Generic;
using System.Linq;

namespace Codewars
{
    class LoopCount
    {
        public class VisitedNode
        {
            public int Count { get; set; }
            public int HashCode { get; set; }
        }

        public static int getLoopSize(LoopDetector.Node startNode)
        {
            //Enter code here.
            var count = 0;
            var visited = new Dictionary<int, int>();
            for (var node = startNode;;node = node.next)
            {
                var hash = node.GetHashCode();
                if (visited.ContainsKey(hash))
                {
                    count -= visited[hash] + 1;
                    break;
                }
                else
                {
                    visited.Add(hash, ++count);
                }
                node = node.next;
            }
            return count;






            ////Enter code here.
            //var count = 0;
            //var ret = 0;
            //var visited = new Dictionary<int, int>();
            //var node = startNode;
            //while (true)
            //{
            //    var hash = node.GetHashCode();
            //    if (visited.ContainsKey(hash))
            //    {
            //        ret = count - visited[hash] + 1;
            //        break;
            //    }
            //    else
            //    {
            //        visited.Add(hash, ++count);
            //    }
            //    node = node.next;
            //}
            //return ret;
        }
    }

    internal class LoopDetector
    {
        internal class Node
        {
            internal Node next;
        }
    }
}
