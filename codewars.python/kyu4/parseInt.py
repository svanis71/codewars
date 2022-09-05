import re


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def find_right_end(nod: TreeNode):
    return nod if not nod.right else find_right_end(nod.right)


def add_node(tree: TreeNode, pnod: TreeNode):
    nod = find_right_end(tree)
    if pnod.value >= 100:
        while nod.left:
            nod = nod.left
        nod.left = pnod
    else:
        nod.right = pnod


def parse_int(s: str) -> int:
    """
        https://www.codewars.com/kata/parseint-reloaded/train/python
    :param s: Number as string
    :return: Number as int
    """
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
               'nine': 9,
               'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
               'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'hundred': 100, 'thousand': 1000, 'million': 1000000,
               'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
               'ninety': 90}

    sm = re.sub(r'\s+and\s+', ' ', s)
    sm = re.sub(r'(-\s+)', '', sm).split(' ')
    tree = None

    for d in sm:
        sp = d.split('-')
        dig = numbers[sp[0]] + (0 if len(sp) == 1 else numbers[sp[1]])
        nod = TreeNode(dig)

        if not tree:
            tree = nod
        else:
            add_node(tree, nod)

    running_sum, tmp, nod = 0, 0, tree
    while nod:
        tmp += nod.value
        leftn = nod.left
        while leftn:
            tmp = tmp * leftn.value
            if leftn.value == 1000:
                running_sum = running_sum + tmp
                tmp = 0
            leftn = leftn.left
        nod = nod.right
    return running_sum + tmp
