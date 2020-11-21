from alphabet_war.alphabet_war_wooloo import alphabet_war
from parseInt import parse_int


def run():
    # print(alphabet_war('[a]#[b]#[c]'))  # ac
    # print(alphabet_war('[a]#b#[c][d]'))  # d
    # print(alphabet_war2('****'))
    # print(alphabet_war2('m**ezdqppmefpdz*gp'))
    print(alphabet_war('zdqmwpbs'))

def run_parseInt():
    print(parse_int('seven hundred thousand'))
    print(parse_int('ninety'))
    print(parse_int('ninety-nine'))
    print(parse_int('ninety-nine thousand'))
    print(parse_int('ninety-nine thousand nine hundred'))
    print(parse_int('ninety-nine thousand nine hundred and ninety-nine'))
    print(parse_int('two hundred three thousand'))
    print(parse_int('two hundred three'))
    print(parse_int('three thousand'))

    print(parse_int('seventy-seven'))
    print(parse_int('zero'))
    print(parse_int('one'))
    print(parse_int('twenty-'))
    print(parse_int('two hundred forty-six'))
    print(parse_int('two hundred and forty-six'))


if __name__ == '__main__':
    run()
