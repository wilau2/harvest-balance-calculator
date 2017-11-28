from datetime import timedelta
from dateutil.parser import parse

from HarvestBalanceCalculator import WorkingPreference


class WorkingTimeInterval:
    def __init__(self, config):
        self.working_preference = WorkingPreference(config)
        self.begin_date = parse(config["beginDate"]).date()
        self.end_date = parse(config["endDate"]).date()

    def get_number_of_working_days(self):
        delta = (self.end_date - self.begin_date)
        number_of_working_days = 0
        for i in range(delta.days + 1):
            date = self.begin_date + timedelta(days=i)
            if self.working_preference.is_a_working_day(date):
                number_of_working_days += 1
        return number_of_working_days

    def get_total_should_of_worked_time(self):
        return self.get_number_of_working_days() * self.working_preference.hours_per_day
