import calendar
import datetime

from opass.workdays import working_days


def calculate_cost(cost, working_days_flag, month, nr_of_passes):
    """Calculate the monthly tolls cost"""
    if working_days_flag:
        passes = working_days(month) * nr_of_passes
    else:
        now = datetime.datetime.now()
        passes = calendar.monthrange(now.year, month)[1] * nr_of_passes
    total_cost = 0

    for i in range(1, passes + 1):
        if 1 <= i <= 5:
            total_cost += cost
        elif 6 <= i <= 10:
            total_cost += cost - (cost * 15 / 100)
        elif 11 <= i <= 20:
            total_cost += cost - (cost * 30 / 100)
        elif 21 <= i <= 30:
            total_cost += cost - (cost * 40 / 100)
        elif 31 <= i <= 40:
            total_cost += cost - (cost * 50 / 100)
        elif 41 <= i <= 60:
            total_cost += cost - (cost * 60 / 100)
        else:
            total_cost += cost
    return total_cost
