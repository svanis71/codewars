import unittest
from typing import Optional

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


def dump(head: Node):
    ptr = head
    while ptr is not None:
        print(f'{ptr.valle} ', end='')
        ptr = ptr.pnext
    print('')


class MyTestCase(unittest.TestCase):
    def test_1(self):
        head = create_nodes(1)
        swap_pairs(head)
        dump(head)

    def test_2(self):
        head = create_nodes(2)
        dump(head)
        head = swap_pairs(head)
        dump(head)

    def test_3(self):
        head = create_nodes(3)
        dump(head)
        head = swap_pairs(head)
        dump(head)

    def test_4(self):
        head = create_nodes(4)
        dump(head)
        head = swap_pairs(head)
        dump(head)

    def test_5(self):
        head = create_nodes(5)
        dump(head)
        head = swap_pairs(head)
        dump(head)


if __name__ == '__main__':
    unittest.main()
