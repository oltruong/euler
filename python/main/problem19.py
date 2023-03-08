import datetime

from lib.measure_time import measure_time


def counting_sundays_with_basic_increment():
    day = datetime.datetime.fromisoformat("1901-01-01")
    final_day = datetime.datetime.fromisoformat("2000-12-31")
    counter = 0

    while day <= final_day:
        if day.day == 1 and day.weekday() == 6:
            counter += 1
        day = day + datetime.timedelta(days=1)
    return counter


def counting_sundays_with_modulo():
    day = (1 + 365) % 7
    days_per_month = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]

    year = 1901
    counter = 0
    while year < 2001:
        month = 1
        while month <= 12:
            day += days_per_month[month - 1]
            if month == 2 and leap_year(year):
                day += 1

            if day % 7 == 0:
                counter += 1
            month += 1
        year += 1
    return counter


def leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def get_problem19():
    modulo=measure_time(counting_sundays_with_modulo)
    basic_increment = measure_time(counting_sundays_with_basic_increment)

    assert modulo==basic_increment
    return basic_increment

