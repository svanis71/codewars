from re import sub


def remove_parentheses(s):
    return s if s.find('(') < 0 else remove_parentheses(sub(r'\([\w\s]*\)', '', s))
