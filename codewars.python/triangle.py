# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/python

def triangle(row):
    row = [0 if c == 'R' else 1 if c == 'G' else 2 for c in row]
    while len(row) > 1:
        row = [a if a == b else 3 - a - b for a, b in zip(row, row[1:])]
    return 'R' if row[0] == 0 else 'G' if row[0] == 1 else 'B'
