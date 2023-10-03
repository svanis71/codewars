import unittest

from kyu6.calendar_week import day_of_week, get_calendar_week


class CalendarWeekTests(unittest.TestCase):
    def test_dow(self):
        self.assertEqual(4, day_of_week(2022, 9, 22))

    def test_dow_2(self):
        self.assertEqual(5, day_of_week(2023, 1, 27))

    def test_week_44_leap_year(self):
        self.assertEqual(44, get_calendar_week("2016-11-05"))

    def test_week_52_1_1(self):
        self.assertEqual(52, get_calendar_week("2017-01-01"))

    def test_week_52_12_24(self):
        self.assertEqual(52, get_calendar_week("2018-12-24"))

    def test_week_1_12_31(self):
        self.assertEqual(1, get_calendar_week("2018-12-31"))

    def test_week_1_1_1(self):
        self.assertEqual(1, get_calendar_week("2019-01-01"))

    def test_week_9_leap(self):
        self.assertEqual(9, get_calendar_week("2016-02-29"))

    def test_week_(self):
        self.assertEqual(53, get_calendar_week("2015-12-29"))


if __name__ == '__main__':
    unittest.main()
