def digital_root(n):
    '''
    https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
    '''
    return n if n < 10 else digital_root(sum([int(i) for i in str(n)]))