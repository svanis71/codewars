"""
    https://www.codewars.com/kata/5865a407b359c45982000036/python
"""
import unittest

from parameterized import parameterized

from kyu5.slogan_maker import slogan_maker


class MyTestCase(unittest.TestCase):
    @parameterized.expand([(["super"], ["super"]),
                           (["super", "hot"], ["super hot", "hot super"]),
                           (["super", "hot", "guacamole"],
                            ["super hot guacamole", "super guacamole hot", "hot super guacamole", "hot guacamole super",
                             "guacamole super hot", "guacamole hot super"]),
                           (["super", "guacamole", "super", "super", "hot", "guacamole"],
                            ["super guacamole hot", "super hot guacamole", "guacamole super hot", "guacamole hot super",
                             "hot super guacamole", "hot guacamole super"]),
                           (["testing", "testing", "testing"], ["testing"])])
    def test_something(self, words: list[str], expected_slogans: list[str]):
        self.assertEqual(expected_slogans, slogan_maker(words))


if __name__ == '__main__':
    unittest.main()
