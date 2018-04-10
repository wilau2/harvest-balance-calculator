import os


class WorkingPreference:
    def __init__(self):
        self.workdays = list(map(int, os.environ['WORK_DAYS_OF_THE_WEEK'].split()))
        self.hours_per_day = float(os.environ['HOURS_PER_WORK_DAY'])

    def is_a_working_day(self, date):
        return True if date.weekday() in self.workdays else False

    def get_hours_per_day(self):
        return self.hours_per_day
