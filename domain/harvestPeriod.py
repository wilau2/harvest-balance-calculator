import calendar

from config.loader import load_configuration_file
from httpclient.harvestApi import HarvestApi
from utils.timeUtils import get_number_of_weeks_between_dates


class HarvestPeriod:
    def __init__(self, begin_date, end_date):
        self.begin_monday = begin_date.week.monday()
        self.end_sunday = end_date.week.sunday()
        self.api = HarvestApi()
        self.config = load_configuration_file('config.json')

    def get_full_weeks_worked_time_entries(self, a_monday, a_sunday):
        if a_monday.weekday() != calendar.MONDAY:
            raise RuntimeError('first param should be a monday')

        if a_sunday.weekday() != calendar.SUNDAY:
            raise RuntimeError('second param should be a sunday')

        if a_monday > a_sunday:
            raise RuntimeError('a_monday should be before a_sunday')

        return self.api.get_user_time_entries(a_monday, a_sunday)

    def get_total_number_of_worked_hours(self):
        time_entries = self.get_full_weeks_worked_time_entries(self.begin_monday, self.end_sunday)
        total_worked_time = 0
        for time_entry in time_entries:
            total_worked_time += time_entry["hours"]
        return total_worked_time

    def get_total_should_of_worked_time(self):
        number_of_weeks_worked = self.__get_number_of_weeks_worked()
        return number_of_weeks_worked * float(self.config["hoursPerWeek"])

    def __get_number_of_weeks_worked(self):
        return get_number_of_weeks_between_dates(self.begin_monday, self.end_sunday) + 1

