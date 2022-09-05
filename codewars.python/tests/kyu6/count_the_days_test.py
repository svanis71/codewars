import unittest
from datetime import datetime
from unittest.mock import patch

from kyu6.count_the_days import count_days


def get_today():
    """
    Mock today
    :return:
    """
    return datetime(2022, 9, 5, 8, 11, 17, 178759)


@patch("kyu6.count_the_days.get_today")
class CountTheDaysTest(unittest.TestCase):
    def test_past(self, today_mock):
        today_mock.side_effect = get_today
        self.assertEqual("The day is in the past!", count_days(datetime(2022, 9, 3, 18, 0)))

    def test_future(self, today_mock):
        today_mock.side_effect = get_today
        self.assertEqual('1 days', count_days(datetime(2022, 9, 6, 18, 0)))

    def test_future_2(self, today_mock):
        today_mock.side_effect = get_today
        self.assertEqual('2 days', count_days(datetime(2022, 9, 6, 23, 0)))

    def test_today(self, today_mock):
        today_mock.side_effect = get_today
        self.assertEqual('Today is the day!', count_days(datetime(2022, 9, 5, 18, 0)))

    def test_microseconds(self, today_mock):
        today_mock.side_effect = get_today
        self.assertEqual('Today is the day!', count_days(datetime(2022, 9, 5, 13, 11, 17, 178635)))


if __name__ == '__main__':
    unittest.main()
