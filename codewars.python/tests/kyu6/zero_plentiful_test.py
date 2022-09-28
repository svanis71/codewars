import unittest


def zero_plentiful(arr):
    zero_groups, zeros = [], []
    while len(arr):
        i = arr.pop(0)
        if i == 0:
            zeros.append(i)
        elif len(zeros) > 0:
            zero_groups.append(zeros)
            zeros = []
        else:
            zeros = []
    if len(zeros) > 0:
        zero_groups.append(zeros)
    return 0 if any(g for g in zero_groups if len(g) < 4) else len(zero_groups)


class ZeroPlentifulTests(unittest.TestCase):
    def test_0(self):
        self.assertEqual(0, zero_plentiful([3]))

    def test_1(self):
        self.assertEqual(1, zero_plentiful([0, 0, 0, 0, 0, 0]))

    def test_2(self):
        self.assertEqual(2, zero_plentiful([0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 4]))

    def test_3(self):
        self.assertEqual(2, zero_plentiful([1, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0]))

    def test_with_10(self):
        self.assertEqual(0, zero_plentiful([10, 0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
