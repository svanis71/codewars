import re


def clean_string(s):
    return s if not '#' in s else clean_string(re.sub(r'.?#', '', s, 1))