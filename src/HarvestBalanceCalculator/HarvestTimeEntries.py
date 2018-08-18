class HarvestTimeEntries:
    def __init__(self, time_entries):
        self.time_entries = time_entries

    def get_total_worked_time(self):
        return sum(time_entry["hours"] for time_entry in self.time_entries)
