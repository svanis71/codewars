def tops(msg):
    """
    https://www.codewars.com/kata/59b7571bbf10a48c75000070/python

                                                          3
                                  p                     2   4
                g               o   q                 1
      b       f   h           n       r             z
    a   c   e       i       m          s          y
          d           j   l             t       x
                        k                 u   w
                                            v

    should return 3pgb

    :param msg: Input string
    :return: tops in reverse order
    """
    top, gap, letters = 1, 5, ''
    while top < len(msg):
        letters += msg[top]
        top, gap = top + gap, gap + 4
    return letters[::-1]
