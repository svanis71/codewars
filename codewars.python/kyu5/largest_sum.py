def largest_sum(arr):
    '''
    https://www.codewars.com/kata/56001790ac99763af400008c/python
    https://en.wikipedia.org/wiki/Maximum_subarray_problem

    :param arr: array of ints
    :return: max subarray value
    '''
    if all(x <= 0 for x in arr):
        return 0
    if all(x > 0 for x in arr):
        return sum(arr)
    maxsum, running_max = float("-inf"), 0
    for val in arr:
        running_max += val
        maxsum = max(maxsum, running_max)
        running_max = max(0, running_max)
    return maxsum
