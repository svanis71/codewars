from datetime import datetime


def get_today():
    return datetime.now()


def count_days(d: datetime) -> str:
    """
    https://www.codewars.com/kata/5837fd7d44ff282acd000157/python
    # of days should be rounded
    :param d: A date
    :return: Number of days to d
    """
    delta = d - get_today()
    days_left = delta.days + round(delta.seconds / 3600 / 24)
    if delta.days == 0:
        return 'Today is the day!'
    return 'The day is in the past!' if days_left < 0 else f'{days_left} days'
