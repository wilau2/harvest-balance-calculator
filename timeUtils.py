import calendar
from datetime import datetime, timedelta
from isoweek import Week


def get_number_of_weeks_between_dates(begin_date, end_date):
    monday1 = (begin_date - timedelta(days=begin_date.weekday()))
    monday2 = (end_date - timedelta(days=end_date.weekday()))
    return (monday2 - monday1).days / 7


def get_monday_from_week_including_date(date):
    week = Week(date.year, get_week_number(date))
    return week.monday()


def get_sunday_from_week_including_date( date):
    week = Week(date.year, get_week_number(date))
    return week.sunday()


def get_week_number(date):
    return int(datetime(date.year, date.month, date.day).strftime("%V"))


def get_day_name_of_week(date):
    return calendar.day_name[date.weekday()]

