from collections import Counter
from itertools import permutations


def slogan_maker(words: list[str]) -> list[str]:
    cnt = Counter(words)
    return [' '.join(x) for x in list(permutations(list(cnt.keys()), r=len(cnt)))]
