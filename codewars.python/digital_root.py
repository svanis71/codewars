def digital_root(num: int) -> int:
    """
    https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
    
    :param num A number
    :return The digital root
    """
    return num if num < 10 else digital_root(sum([int(i) for i in str(num)]))
