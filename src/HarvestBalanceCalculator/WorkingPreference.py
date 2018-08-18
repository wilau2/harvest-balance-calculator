import os


class WorkingPreference:
    def __init__(self):
        self.workdays = [float(work_day) for work_day in os.environ['WORK_DAYS_OF_THE_WEEK'].split()]
        self.hours_per_day = float(os.environ['HOURS_PER_WORK_DAY'])

    def is_a_working_day(self, date):
        return date.weekday() in self.workdays

    def get_hours_per_day(self):
        return self.hours_per_day
