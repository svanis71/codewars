import re


def clean_string(dirty_string: str) -> str:
    """
    :param s String to clean
    :return A clean string
    """
    return dirty_string if not '#' in dirty_string else clean_string(re.sub(r'.?#', '', dirty_string, 1))
