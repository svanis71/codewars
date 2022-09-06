from collections import defaultdict
from textwrap import wrap
from _md5 import md5


class UrlShortener:
    def __init__(self):
        self.next = 1
        self.shortlong = defaultdict(str)

    def shorten(self, long_url):
        ahash = md5(long_url.encode('ascii')).hexdigest()[-8:]
        short_url = ''.join([chr(97 + int(c, 16) % 26) for c in wrap(ahash, 2)])
        self.shortlong[short_url] = long_url
        return 'short.ly/' + short_url

    def redirect(self, short_url):
        return self.shortlong[short_url[-4:]]
