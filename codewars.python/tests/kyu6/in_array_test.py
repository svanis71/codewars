import unittest


def in_array(array1: list, array2: list) -> list:
    return sorted(set(ts for ts in array1 if any(s for s in array2 if ts in s)))


class InArrayTests(unittest.TestCase):
    def test_something(self):
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        actual = in_array(a1, a2)
        self.assertEqual(actual, r)

    def test_2(self):
        a1 = ["arp", "mice", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        actual = in_array(a1, a2)
        self.assertEqual(actual, r)

    def test_duplicates(self):
        a1 = ["arp", "arp", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        actual = in_array(a1, a2)
        self.assertEqual(actual, r)


if __name__ == '__main__':
    unittest.main()
