import ctypes
import unittest
from textwrap import wrap


class UrlShortener:
    def __init__(self):
        self.shortlong = {}

    @staticmethod
    def hashu(word):
        return ctypes.c_uint64(hash(word)).value

    def hashn(self, word, number_of_bytes):
        return (self.hashu(word) % (2 ** (number_of_bytes * 8))).to_bytes(number_of_bytes, "big").hex()

    def shorten(self, long_url):
        urlhash = self.hashn(long_url, 4)
        short_url = ''.join([chr(97 + int(c, 16) % 26) for c in wrap(urlhash, 2)])
        if short_url not in self.shortlong:
            self.shortlong[short_url] = long_url
        return 'short.ly/' + short_url

    def redirect(self, short_url):
        return self.shortlong[short_url[-4:]]


class UrlShortenerTests(unittest.TestCase):

    @staticmethod
    def test_something():
        us = UrlShortener()
        print(us.shorten('http://foo.se/search'))
        print(us.shorten('http://foo.se/search'))
        print(us.shorten('http://foo.se/search?q=apa'))
        print(us.shorten('http://foo.se/search?a=dsfg'))
        print(us.shorten('http://foo.se/search?q=dsghrs'))
        print(us.shorten('http://foo.se/search?q=dfghd'))


if __name__ == '__main__':
    unittest.main()
