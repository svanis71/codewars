import unittest


def subsequence_sums(arr, s):
    """
    https://www.codewars.com/kata/60df63c6ce1e7b0023d4af5c/train/python

    :param arr: array of ints -10000 <= x <= 10000
    :param s: Value to test against
    :return: Number of subsequences that sums to testval
    """

    # map = defaultdict(list)
    running_sum = 0
    # sliding_sum = 0
    cnt = 0
    for v in arr:
        running_sum += v
        if s in (v, running_sum):
            cnt += 1

    # map = {}
    # sum = 0
    # for i, v in enumerate(arr):
    #     sum += v
    #     if sum in map:
    #         print(map[sum][0] + 1, "to", i)
    #     map[sum] = (i, sum)

    # cnt, summa = 0, 0
    # for idx, v1 in enumerate(arr):
    #     if v1 == s:
    #         cnt += 1
    #     sum = v1
    #     for v2 in arr[idx+1:]:
    #         sum += v2
    #         if sum == s:
    #             cnt += 1
    #         if -10000 > sum > 10000:
    #             sum = 0
    return 0


class SubSequenceSumTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, subsequence_sums([1, 2, 3, -3, -2, -1], 0))

    def test_2(self):
        self.assertEqual(4, subsequence_sums([1, 5, -2, 4, 0, -7, -3, 6], 4))

    def test_3(self):
        self.assertEqual(2, subsequence_sums([9, -2, -5, 8, 6, -10, 0, -4], -1))


if __name__ == '__main__':
    unittest.main()
