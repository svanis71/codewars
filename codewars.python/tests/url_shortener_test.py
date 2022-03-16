import unittest

from url_shortener import Url_shortener


class MyTestCase(unittest.TestCase):

    def test_something(self):
        us = Url_shortener()
        print(us.shorten('http://foo.se/search'))
        print(us.shorten('http://foo.se/search'))
        print(us.shorten('http://foo.se/search?q=apa'))
        print(us.shorten('http://foo.se/search?a=dsfg'))
        print(us.shorten('http://foo.se/search?q=dsghrs'))
        print(us.shorten('http://foo.se/search?q=dfghd'))


if __name__ == '__main__':
    unittest.main()
