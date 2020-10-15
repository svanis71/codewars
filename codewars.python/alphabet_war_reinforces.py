def alphabet_war(reinforces, airstrikes):
# The battlefield  is     : "abcedfg".
# The first airstrike    : "   *   "
# After first airstrike  : "ab___fg"
# Reinforces are comming : "abjklfg"
# The second airstrike   : "*  *   "
# After second airstrike : "_____fg"
# Reinforces are coming  : "hi___fg"
# No more airstrikes => return "hi___fg"

    battlefield = reinforces[0]
    for i, airstrike in enumerate(airstrikes):
        # strike
        pos = airstrike.find('*')
        removefrom = 0 if pos == 0 else pos - 1
        removeto = pos + 1
        n = removeto - removefrom
        battlefield = battlefield[0:removefrom] + '_'*n + battlefield[removeto:]
        # reinforce
        battlefield = reinforces
    return ''





class Test:
    def assert_equals(self, acutal, expected_result):
        print('OK' if acutal == expected_result else 'Expect %s to equal %s' % (acutal, expected_result))
        return True if acutal == expected_result else False


test = Test()

test.assert_equals(alphabet_war(["abcdefg", "hijklmn"], ["   *   ", "*  *   "]), 'hi___fg');
# test.assert_equals(alphabet_war(["aaaaa", "bbbbb", "ccccc", "ddddd"], ["*", " *", "   "]), 'ccbaa');

reinforces = ["g964xxxxxxxx",
              "myjinxin2015",
              "steffenvogel",
              "smile67xxxxx",
              "giacomosorbi",
              "freywarxxxxx",
              "bkaesxxxxxxx",
              "vadimbxxxxxx",
              "zozofouchtra",
              "colbydauphxx"]
airstrikes = ["* *** ** ***",
              " ** * * * **",
              " * *** * ***",
              " **  * * ** ",
              "* ** *   ***",
              "***   ",
              "**",
              "*",
              "*"]

# test.assert_equals(alphabet_war(reinforces, airstrikes), 'codewarsxxxx', 'Top 50 massacre failure');
