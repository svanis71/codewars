from datetime import datetime

days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def is_leap_year(yr: int) -> bool:
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)


def day_of_week(year: int, month: int, day: int) -> int:
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return int((year + year / 4 - year / 100 + year / 400 + t[month - 1] + day)) % 7


def day_of_year(date_string: str):
    year, month, day = [int(n) for n in date_string.split('-')]
    leap_days = 1 if is_leap_year(year) and month > 2 else 0
    doy = days[month - 1] + day + leap_days
    return doy, day_of_week(year, month, day)


def get_calendar_week(date_string: str) -> int:
    return datetime.fromisoformat(date_string).isocalendar().week
