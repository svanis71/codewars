import unittest
from typing import Optional

from parameterized import parameterized

from kyu5.swap_pairs import swap_pairs, Node


def create_nodes(num: int) -> Optional[Node]:
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num == 0:
        return None
    head = Node(abc[0])
    n, cnt = head, 1
    while cnt < num:
        n.pnext = Node(abc[cnt])
        n = n.pnext
        cnt += 1
    return head


def dump(head: Node) -> str:
    plist, ptr = '', head

    while ptr is not None:
        plist += f'{" -> " if plist != "" else ""}{ptr.valle}'
        ptr = ptr.pnext
    return plist


class MyTestCase(unittest.TestCase):

    @parameterized.expand([(0, ''),
                           (1, 'A'),
                           (2, 'B -> A'),
                           (3, 'B -> A -> C'),
                           (4, 'B -> A -> D -> C'),
                           (5, 'B -> A -> D -> C -> E')])
    def test_swap(self, numnodes: int, expected: str):
        head = create_nodes(numnodes)
        head = swap_pairs(head)
        self.assertEqual(expected, dump(head))


if __name__ == '__main__':
    unittest.main()
