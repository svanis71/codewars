import unittest

from build_tower_adv import tower_builder


class BuildTowerAdvTests(unittest.TestCase):
    def test_simplest(self):
        self.assertEqual(tower_builder(1, (1, 1)), ['*', ])

    def test_something(self):
        self.assertEqual(tower_builder(3, (4, 2)),
                         ['        ****        ', '        ****        ', '    ************    ',
                          '    ************    ', '********************', '********************'])


# 2 * floors - 1
if __name__ == '__main__':
    unittest.main()
