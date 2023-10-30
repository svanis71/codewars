import unittest

from parameterized import parameterized

from kyu5.brainscrambler import Interpreter


class BrainScramblerTestCase(unittest.TestCase):
    interpreter = Interpreter()

    @parameterized.expand([('*.', '0', 'Addition/subtraction test'),
                           ('*++.', '2', 'Addition/subtraction test'),
                           ('*+-.', '0', 'Addition/subtraction test'),
                           ('*+*.', '0', 'Addition/subtraction test'),
                           ('*+++-+.', '3', 'Addition/subtraction test'),
                           ('####*.', '0', 'Rotation tests'),
                           ('*.#*+.#*++.#.', '0120', 'Rotation tests'),
                           ('*++>#.', '2', 'Rotation tests'),
                           ('*+++<##.', '3', 'Rotation tests'),
                           ('***++-+>#>#>#.', '2', 'Rotation tests'),
                           (',5[.-]', '54321', 'Loop tests'),
                           (',9[.-]', '987654321', 'Loop tests'),
                           (',10>*#[-##.+#]', '0123456789', 'Loop tests'),
                           (',4>*++#[-##.++#]', '2468', 'Loop tests'),
                           (',9[.--]', '97531', 'Loop tests')
                           ])
    def test_something(self, code, expected, msg):
        result: str = self.interpreter.read(code)
        self.assertEqual(expected, result, f'{msg}: {code} expects to be {expected}')


if __name__ == '__main__':
    unittest.main()
