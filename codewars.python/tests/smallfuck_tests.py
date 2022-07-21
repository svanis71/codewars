import unittest

from smallfuck import interpreter


class SmallFuckTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(interpreter("*", "00101100"), "10101100")
        # Flips the second and third cell of the tape
        self.assertEqual(interpreter(">*>*", "00101100"), "01001100")
        # Flips all the bits in the tape
        self.assertEqual(interpreter("*>*>*>*>*>*>*>*", "00101100"), "11010011")
        # Flips all the bits that are initialized to 0
        self.assertEqual(interpreter("*>*>>*>>>*>*", "00101100"), "11111111")
        # Goes somewhere to the right of the tape and then flips all bits that are initialized to 1,
        # progressing leftwards through the tape
        self.assertEqual(interpreter(">>>>>*<*<<*", "00101100"), "00000000")

    def test_ignore_invalido_instructions(self):
        self.assertEqual(interpreter(">>nssewww>>wwess>*<nnn*<<ee*", "00101100"), "00000000")

    def test_simple_loop(self):
        self.assertEqual(interpreter("*[>*]", "0" * 256), "1" * 256)

    def test_nested_loops(self):
        self.assertEqual('10101', interpreter('[>[*>*>*>]>]', '10110'))


if __name__ == '__main__':
    unittest.main()
