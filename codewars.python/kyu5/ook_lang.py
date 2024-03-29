def okkOokOo(code):
    return ''.join([TRANSLATIONS[letter.strip()] for letter in code[0:-1].split('?')])


TRANSLATIONS = {
    'Ok, Oooook': 'A',
    "Ok, Ooook, O": "B",
    "Ok, Oook, Oo": "D",
    "Ok, Oook, Ok": "E",
    "Ok, Oookkk": "G",
    'Ok, Ook, Ooo': 'H',
    "Ok, Ook, Ook": "I",
    'Ok, Ook, Ok, O': 'J',
    'Ok, Ook, Okk': 'K',
    "Ok, Ookk, Oo": "L",
    'Ok, Ookk, Ok': 'M',
    "Ok, Ookkkk": "O",
    "Ok, Ok, Oooo": "P",
    "Ok, Ok, Ook, O": "R",
    "Ok, Ok, Ookk": "S",
    "Ok, Ok, Ok, Oo": "T",
    "Ok, Ok, Ok, Ok": "U",
    'Ok, Ok, Okkk': 'W',
    "Ok, Okk, Ook": "Y",
    "Okk, Ooook": "a",
    "Okk, Oook, O": "b",
    "Okk, Oookk": "c",
    'Okk, Ook, Ok': 'e',
    'Okk, Ook, Oo': 'd',
    'Okk, Ookkk': 'g',
    "Okk, Ok, Ooo": "h",
    "Okk, Ok, Ook": "i",
    "Okk, Ok, Okk": "k",
    'Okk, Okk, Oo': 'l',
    "Okk, Okk, Ok": "m",
    "Okk, Okkk, O": "n",
    'Okk, Okkkk': 'o',
    'Okkk, Oooo': 'p',
    'Okkk, Ook, O': 'r',
    'Okkk, Ookk': 's',
    'Okkk, Ok, Oo': 't',
    "Okkk, Ok, Ok": "u",
    "Okkkk, Ooo": "x",
    "Okkkk, Ook": "y",
    'Ook, Ooook': '!',
    "Ok, Ookkk": "'",
    'Ok, Ooooo': ' ',
    'Ok, Okk, Ok': '-',
    "Ook, Okk, Oo": ",",
}
