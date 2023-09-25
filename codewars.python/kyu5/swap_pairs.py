"""
https://www.codewars.com/kata/59c6f43c2963ecf6bf002252/python
"""


class Node:
    def __init__(self, val: str, pnext=None):
        self.valle = val
        self.pnext = pnext


def swap_pairs(head):
    if head is None or head.pnext is None:
        return head
    newhead = head.pnext
    ptr, tail = head, None
    while ptr and ptr.pnext:
        left, right, ptr = ptr, ptr.pnext, ptr.pnext.pnext
        left.pnext, right.pnext = ptr, left
        if tail:
            tail.pnext = right
        tail = left
    return newhead
