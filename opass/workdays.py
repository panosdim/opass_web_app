#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
# ---------------------------------------------------------------------------
# Calculate working days of a month taking into account Greek Bank Holidays
#
# Copyright 2018 Panagiotis Dimopoulos (panosdim@gmail.com)
#
# Version: 1.0
# ---------------------------------------------------------------------------

import calendar
import datetime


def orthodox_easter(year):
    r1 = year % 4
    r2 = year % 7
    r3 = year % 19
    r4 = (19 * r3 + 15) % 30
    r5 = (2 * r1 + 4 * r2 + 6 * r4 + 6) % 7
    days = r5 + r4 + 13

    if days > 39:
        days = days - 39
        oed = datetime.date(year, 5, days)
    elif days > 9:
        days = days - 9
        oed = datetime.date(year, 4, days)
    else:
        days = days + 22
        oed = datetime.date(year, 3, days)

    return oed


def bank_holidays(year):
    holidays = []
    new_year_eve = datetime.date(year, 1, 1)
    epiphany = datetime.date(year, 1, 6)
    easter = orthodox_easter(year)
    clean_monday = easter - datetime.timedelta(48)
    independence_day = datetime.date(year, 3, 25)
    good_friday = easter - datetime.timedelta(2)
    easter_monday = easter + datetime.timedelta(1)
    labour_day = datetime.date(year, 5, 1)
    whit_monday = easter + datetime.timedelta(50)
    assumption = datetime.date(year, 8, 15)
    ochi_day = datetime.date(year, 10, 28)
    christmas = datetime.date(year, 12, 25)
    glorifying = datetime.date(year, 12, 26)
    holidays.append(new_year_eve)
    holidays.append(epiphany)
    holidays.append(clean_monday)
    holidays.append(independence_day)
    holidays.append(good_friday)
    holidays.append(easter_monday)
    holidays.append(labour_day)
    holidays.append(whit_monday)
    holidays.append(assumption)
    holidays.append(ochi_day)
    holidays.append(christmas)
    holidays.append(glorifying)

    return holidays


def working_days(month):
    business_days = 0
    cal = calendar.Calendar()
    now = datetime.datetime.now()
    holidays = bank_holidays(now.year)

    for week in cal.monthdayscalendar(now.year, month):
        for i, day in enumerate(week):
            # not this month's day or a weekend
            if day == 0 or i >= 5:
                continue
            # or a holiday
            this_date = datetime.date(now.year, month, day)
            if this_date in holidays:
                continue
            business_days += 1

    return business_days
