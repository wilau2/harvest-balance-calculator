import setup
from HarvestBalanceCalculator import WorkingTimeInterval, HarvestTimeEntries
from HarvestHttpClient.Client import HarvestHttpClient

working_time_interval = WorkingTimeInterval()

total_should_have_worked_time = working_time_interval.get_total_should_have_worked_time()

print("total_should_have_worked_time")
print(total_should_have_worked_time)

harvest_http_client = HarvestHttpClient()
user_id = harvest_http_client.get_me()["id"]

time_entries = harvest_http_client.get_user_time_entries(
    working_time_interval.begin_date,
    working_time_interval.end_date,
    user_id
)

harvest_time_entries = HarvestTimeEntries(time_entries)
total_worked_time = harvest_time_entries.get_total_worked_time()

print("total_worked_time")
print(total_worked_time)

diff = total_worked_time - total_should_have_worked_time
if diff > 0:
    print("You have some over time")
    print(diff)
else:
    print("You owe big brother")
    print(diff)
