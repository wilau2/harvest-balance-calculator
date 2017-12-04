from datetime import timedelta
from dateutil.parser import parse

from HarvestBalanceCalculator import WorkingPreference


class WorkingTimeInterval:
    def __init__(self, config):
        self.working_preference = WorkingPreference(config)
        self.begin = parse(config["period"]["begin"]).date()
        self.end = parse(config["period"]["end"]).date()

    def get_number_of_working_days(self):
        delta = (self.end - self.begin)
        number_of_working_days = 0
        for i in range(delta.days + 1):
            date = self.begin + timedelta(days=i)
            if self.working_preference.is_a_working_day(date):
                number_of_working_days += 1
        return number_of_working_days

    def get_total_should_of_worked_time(self):
        return self.get_number_of_working_days() * self.working_preference.hours_per_day

    def get_date_range(self):
        for n in range(int((self.end + timedelta(days=1) - self.begin).days)):
            yield self.begin + timedelta(n)
