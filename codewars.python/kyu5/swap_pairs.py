"""
https://www.codewars.com/kata/59c6f43c2963ecf6bf002252/python
"""
from typing import Optional


class Node:
    def __init__(self, val: str, pnext=None):
        self.valle = val
        self.pnext = pnext


def swap_pairs(head: Node) -> Optional[Node]:
    if head is None or head.pnext is None:
        return head
    newhead, ptr, tail = head.pnext, head, None
    while ptr and ptr.pnext:
        left, right, ptr = ptr, ptr.pnext, ptr.pnext.pnext
        left.pnext, right.pnext = ptr, left
        if tail:
            tail.pnext = right
        tail = left
    return newhead
