from Config.Loader import load_configuration_file


class WorkingPreference:
    def __init__(self, config_loader=load_configuration_file):
        config = config_loader('config.json')
        self.preference = config["preference"]
        self.workdays = self.preference["daysOfWork"]
        self.hours_per_day = float(self.preference["hoursPerDay"])

    def is_a_working_day(self, date):
        return True if date.weekday() in self.workdays else False

    def get_hours_per_day(self):
        return self.hours_per_day
