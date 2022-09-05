def validate_word(word: str) -> bool:
    """
    https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

    :param word The word
    :return True if ok
    """
    word = word.lower()
    return len(set(word.count(c) for c in (set(word)))) == 1
