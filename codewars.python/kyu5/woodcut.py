def wood_cut(woods, n):
    '''
    https://www.codewars.com/kata/583dbc028bbc0446f500032b/train/python

    :param woods: Array of woods
    :param n: How many pieces
    :return: Longest possible piece
    '''
    low, high = 1, max(woods)
    while (low <= high):
        mid = low + (high - low) // 2
        if (sum(x // mid for x in woods) >= n):
            low = mid + 1
        else:
            high = mid - 1
    return high
