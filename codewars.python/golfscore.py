def golf_score_calculator(par_string, score_string):
    '''
    https://www.codewars.com/kata/59f7a0a77eb74bf96b00006a/train/python

    :param par_string: pars
    :param score_string: your score
    :return: your score against par
    '''
    return sum(int(score) - int(par) for (par, score) in zip(list(par_string), list(score_string)))
