def alphabet_war_reinforces(reinforces, airstrikes):
    """
        Doesn't work

        https://www.codewars.com/kata/593e2077edf0d3e2d500002d

        Task
        Write a function that accepts reinforces array of strings and airstrikes array of strings.
        The reinforces strings consist of only small letters. The size of each string in reinforces array is the same.
        The airstrikes strings consists of * and white spaces. The size of each airstrike may vary. There may be also no airstrikes at all.

        The first row in reinforces array is the current battlefield. Whenever some letter is killed by bomb, it's replaced by a letter from next string in reinforces array on the same position.
        The airstrike always starts from the beginning of the battlefield.
        The * means a bomb drop place. The each * bomb kills letter only on the battelfield. The bomb kills letter on the same index on battlefield plus the adjacent letters.
        The letters on the battlefield are replaced after airstrike is finished.
        Return string of letters left on the battlefield after the last airstrike. In case there is no any letter left in reinforces on specific position, return _.

        reinforces = [ "abcdefg",
                    "hijklmn"];
        airstrikes = [ "   *   ",
                    "*  *   "];
                    
        The battlefield  is     : "abcdefg".
        The first airstrike    : "   *   "  
        After first airstrike  : "ab___fg"
        Reinforces are comming : "abjklfg"
        The second airstrike   : "*  *   "
        After second airstrike : "_____fg"
        Reinforces are coming  : "hi___fg"
        No more airstrikes => return "hi___fg"

    :param reinforces:
    :param airstrikes:
    :return:
    """
    battlefield = reinforces.pop(0)
    for i, airstrike in enumerate(airstrikes):
        orig_battlefield = battlefield
        # strike
        removefrom, removeto, reinforce_list = 0, 0, []
        bombs = [i for i, ch in enumerate(airstrike) if ch == '*']
        for pos in bombs:
            removefrom = 0 if pos == 0 else pos - 1
            removeto = pos if pos == len(battlefield) - 1 else  pos + 1
            n = removeto - removefrom + 1
            reinforce_list = reinforce_list + list(range(removefrom, removeto + 1))
            battlefield = battlefield[0:removefrom] + '_'*n + battlefield[removeto+1:]
        
        # reinforce
        reinforce_string = ''
        for rp in [i for i, ch in enumerate(battlefield) if ch == '_']:
            rsrp = '_'
            print(f'{rp}')
            for i, rs in enumerate(reinforces):
                print(f'rs[rp]: {rs} - {rp}')
                if rs[rp] != '_':
                    rsrp = rs[rp]
                    reinforces[i] = ''.join([c if i != rp else '_' for i, c in enumerate(rs)])
                    break
            reinforce_string += rsrp
        
        battlefield = battlefield if reinforce_string == '' else  battlefield[0:removefrom] + reinforce_string + battlefield[removeto+1:]
        # reinforcepos = [i for i, ch in enumerate(battlefield) if ch == '_']
        # reinforce_string = ''
        # for rp in reinforcepos:

    return battlefield

