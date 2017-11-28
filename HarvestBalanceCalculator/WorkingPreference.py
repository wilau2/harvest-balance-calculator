class WorkingPreference:
    def __init__(self, config):
        self.config = config
        self.workdays = config["workDaysOfTheWeek"]
        self.hours_per_day = float(config["hoursPerWorkDay"])

    def is_a_working_day(self, date):
        return True if date.weekday() in self.workdays else False

    def get_hours_per_day(self):
        return self.hours_per_day
