def tower_builder(n_floors):
    """
    https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
    :param n_floors: number of floors
    :return: A tower
    """
    return [('*' * i).center(n_floors * 2 - 1, ' ') for i in range(1, n_floors * 2, 2)]
