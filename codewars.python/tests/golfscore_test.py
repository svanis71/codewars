import unittest

from golfscore import golf_score_calculator


class GolfScoreCalcTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(-1, golf_score_calculator('443454444344544443', '353445334534445344'),
                         'One under par!')  # add assertion here


if __name__ == '__main__':
    unittest.main()
