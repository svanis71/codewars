import unittest

from parameterized import parameterized

from kyu6.cat_and_mouse import cat_mouse


class CatAndMouseTest(unittest.TestCase):
    @parameterized.expand([('..D.....C.m', 2, 'Caught!'),
                           ('............C.............D..m...', 8, 'Escaped!'),
                           ('m.C...', 5, 'boring without all three'),
                           ('.CD......m.', 10, 'Protected!'),
                           ('.CD......m.', 1, 'Escaped!'),
                           ('.........m...........CD.', 18, 'Caught!')])
    def test_something(self, x: str, j: int, expected_result: str):
        self.assertEqual(expected_result, cat_mouse(x, j))


if __name__ == '__main__':
    unittest.main()
