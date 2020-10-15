lefts, rights = ('wpbs', 'mqdz')
wooloo = {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z', 'm': 'w', 'q': 'p', 'd': 'b', 'z': 's'}


def is_priest(letter):
    return letter != '' and letter in 'jt'


def is_opponent(priest, letter):
    if priest == 'j':
        return letter in lefts
    return letter in rights


def is_between_priests(prev, next):
    return is_priest(prev) and is_priest(next) and prev != next


def alphabet_war(fight):
    target = fight
    for i, letter in enumerate(fight):
        if letter in 'jt':
            continue
        prev = fight[i - 1 if i > 0 else 0]
        next = fight[i + 1:i + 2]
        if not is_between_priests(prev, next) and ((is_priest(prev) and is_opponent(prev, letter)) or (
                is_priest(next) and is_opponent(next, letter))):
            target = target[0:i] + wooloo[letter] + target[i + 1:]

    score_right = sum([4 - rights.find(x) for x in target if x in rights])
    score_left = sum([4 - lefts.find(x) for x in target if x in lefts])
    return ['Let\'s fight again!', ['Right side wins!', 'Left side wins!'][score_left > score_right]][
        score_right != score_left]


class Test:
    def assert_equals(self, acutal, expected_result):
        print('OK' if acutal == expected_result else 'Expect %s to equal %s' % (acutal, expected_result))
        return True if acutal == expected_result else False


test = Test()

test.assert_equals(alphabet_war("z"), "Right side wins!")
test.assert_equals(alphabet_war("zm"), "Right side wins!")
test.assert_equals(alphabet_war("zmq"), "Right side wins!")
test.assert_equals(alphabet_war("tz"), "Left side wins!")
test.assert_equals(alphabet_war("jbdt"), "Let's fight again!")
test.assert_equals(alphabet_war("jz"), "Right side wins!")
test.assert_equals(alphabet_war("azt"), "Left side wins!")
test.assert_equals(alphabet_war("wololooooo"), "Left side wins!")
test.assert_equals(alphabet_war("ztztztzs"), "Left side wins!")
test.assert_equals(alphabet_war("mdtjtms"), "Left side wins!")
test.assert_equals(alphabet_war("besbjjw"), "Right side wins!")
test.assert_equals(alphabet_war("zt"), "Left side wins!")
test.assert_equals(alphabet_war("sj"), "Right side wins!")
test.assert_equals(alphabet_war("zdqmwpbs"), "Let's fight again!")
test.assert_equals(alphabet_war("tzj"), "Right side wins!")
test.assert_equals(alphabet_war("mmcjwtqdpzjsjbcpwzzzabmdb"), "Right side wins!")
