import os

from datetime import timedelta
from dateutil.parser import parse

from HarvestBalanceCalculator import WorkingPreference


def count(iterator):
    return sum(1 for _ in iterator)


class WorkingTimeInterval:
    def __init__(self):
        self.working_preference = WorkingPreference()
        self.begin_date = parse(os.environ['BEGIN_DATE']).date()
        self.end_date = parse(os.environ['END_DATE']).date()
        self.worked_hours_correction = float(os.getenv('WORKED_HOURS_CORRECTION', 0))

    def get_number_of_working_days(self):
        return count(day
                     for day in self._days_in_interval()
                     if self.working_preference.is_a_working_day(day))

    def _days_in_interval(self):
        delta = (self.end_date - self.begin_date)
        for i in range(delta.days + 1):
            yield self.begin_date + timedelta(days=i)

    def get_total_should_have_worked_time(self):
        return self.get_number_of_working_days() * self.working_preference.hours_per_day

    def get_worked_hours_correction(self):
        return self.worked_hours_correction
