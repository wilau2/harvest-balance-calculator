from dateutil.parser import parse
from isoweek import Week
from datetime import datetime


class DateStructure:

    def __init__(self, date_string):
        date = parse(date_string).date()
        self.date = date
        self.week = Week(date.year, self.__get_week_number(date))

    @staticmethod
    def __get_week_number(date):
        return int(datetime(date.year, date.month, date.day).strftime("%V"))
