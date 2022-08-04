import ctypes
import unittest
from textwrap import wrap


class Url_shortener:
    def __init__(self):
        self.shortlong = dict()

    def shorten(self, long_url):
        hashu = lambda word: ctypes.c_uint64(hash(word)).value
        hashn = lambda word, N: (hashu(word) % (2 ** (N * 8))).to_bytes(N, "big").hex()
        urlhash = hashn(long_url, 4)
        short_url = ''.join([chr(97 + int(c, 16) % 26) for c in wrap(urlhash, 2)])
        if short_url not in self.shortlong:
            self.shortlong[short_url] = long_url
        return 'short.ly/' + short_url

    def redirect(self, short_url):
        return self.shortlong[short_url[-4:]]

class UrlShortenerTests(unittest.TestCase):

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
