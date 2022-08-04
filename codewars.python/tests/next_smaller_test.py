import unittest


def next_smaller(n):
    digits = [int(c) for c in str(n)]
    if n < 21 or digits == sorted(digits):
        return -1
    result, first_smallest_pos, next_smallest_pos, next_smallest = [], len(digits) - 1, -1, -1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            first_smallest_pos -= 1
            break
        first_smallest_pos -= 1

    for i in range(first_smallest_pos, len(digits)):
        if digits[i] < digits[first_smallest_pos] and digits[i] > next_smallest:
            next_smallest = digits[i]
            next_smallest_pos = i

    digits[first_smallest_pos], digits[next_smallest_pos] = digits[next_smallest_pos], digits[first_smallest_pos]
    tail = sorted(digits[first_smallest_pos + 1:], reverse=True)
    result = [*digits[0:first_smallest_pos + 1], *tail]
    return int(''.join(str(x) for x in result)) if result[0] > 0 else -1


class NextSmallerTests(unittest.TestCase):
    def test_next_smaller_1(self):
        self.assertEqual(-1, next_smaller(3))

    def test_next_smaller_2(self):
        self.assertEqual(next_smaller(907), 790)

    def test_next_smaller_970(self):
        self.assertEqual(next_smaller(970), 907)

    def test_next_smaller_3(self):
        self.assertEqual(next_smaller(531), 513)

    def test_next_smaller_4(self):
        self.assertEqual(next_smaller(511), 151)

    def test_next_smaller_5(self):
        self.assertEqual(next_smaller(135), -1)

    def test_next_smaller_6(self):
        self.assertEqual(next_smaller(2071), 2017)

    def test_next_smaller_7(self):
        self.assertEqual(next_smaller(414), 144)

    def test_next_smaller_8(self):
        self.assertEqual(next_smaller(123456798), 123456789)

    def test_next_smaller_9(self):
        self.assertEqual(next_smaller(123456789), -1)

    def test_next_smaller_10(self):
        self.assertEqual(next_smaller(1234567908), 1234567890)


if __name__ == '__main__':
    unittest.main()
