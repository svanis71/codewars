import re


def trump_detector(trump_speech):
    trumps = sum([len(x) for w, x in re.findall(r'([aouie])(\1+)', trump_speech, re.IGNORECASE)])
    vowels = len(re.findall(r'([aouie])(?!\1)', trump_speech, re.IGNORECASE))
    return round(trumps / vowels, 2)

