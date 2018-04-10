class HarvestTimeEntries:
    def __init__(self, time_entries):
        self.time_entries = time_entries

    def get_total_worked_time(self):
        total_worked_time = 0
        for time_entry in self.time_entries:
            total_worked_time += time_entry["hours"]
        return total_worked_time
