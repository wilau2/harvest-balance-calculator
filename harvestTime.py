from datetime import datetime, timedelta


class HarvestTime:
    @staticmethod
    def create_datetime(year, month, day):
        return datetime(year, month, day)

    @staticmethod
    def get_number_of_weeks_between_dates(d1, d2):
        monday1 = (d1 - timedelta(days=d1.weekday()))
        monday2 = (d2 - timedelta(days=d2.weekday()))
        return (monday2 - monday1).days / 7

    def get_week_begin_and_start(self, date):
        week = int(date.strftime("%V"))
        d = self.create_datetime(date.year, 1, 1)
        d = d - timedelta(d.weekday())
        dlt = timedelta(days=(week - 1) * 7)
        return d + dlt, d + dlt + timedelta(days=6)

    def get_begin_of_week(self, date):
        return self.get_week_begin_and_start(date)[0]

    def get_end_of_week(self, date):
        return self.get_week_begin_and_start(date)[1]