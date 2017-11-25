import http.client
import json

from banner import print_banner
from configurationLoader import load_configuration_file
from harvestTime import HarvestTime

secret_config = load_configuration_file('config.json.secret')
config = load_configuration_file('config.json')

print_banner()

harvest_time = HarvestTime()

begin_year = int(input("begin year (default 2017): ") or "2017")
begin_month = int(input("begin month (default 1): ") or "1")
begin_day = int(input("begin day (default 1): ") or "1")
begin_date = harvest_time.create_datetime(begin_year, begin_month, begin_day)

print(" ")
print("The beginning date is: ")
print(begin_date.isoformat())
print(" ")

end_year = int(input("end year (default 2017): ") or "2017")
end_month = int(input("end month (default 1): ") or "1")
end_day = int(input("end day (default 1): ") or "1")
end_date = harvest_time.create_datetime(end_year, end_month, end_day)

print(" ")
print("The ending date is: ")
print(end_date.isoformat())
print(" ")

headers = {
    "Harvest-Account-ID": secret_config["harvest"]["accountId"],
    "Authorization": secret_config["harvest"]["authorization"],
    "User-Agent": "Harvest API Example"
}
print(headers)
conn = http.client.HTTPSConnection("api.harvestapp.com")

dateFrom = harvest_time.get_begin_of_week(begin_date)
dateTo = harvest_time.get_end_of_week(end_date)

routes = ["/v2/time_entries?from=" + str(dateFrom.isoformat()) + "&to=" + str(dateTo.isoformat())]

time_entries = []
while len(routes) > 0:
    conn.request("GET", routes.pop(), None, headers)
    response = json.loads(conn.getresponse().read())

    time_entries += response["time_entries"]

    next = response["links"]["next"]
    if next:
        routes.append(next)

total_worked_time = 0
for time_entry in time_entries:
    total_worked_time += time_entry["hours"]

number_of_weeks = harvest_time.get_number_of_weeks_between_dates(dateFrom, dateTo)

total_should_of_worked_time = (number_of_weeks + 1) * float(config["hoursPerWeek"])

diff = total_worked_time - total_should_of_worked_time

print("")

if diff > 0:
    print("You have some over time")
    print(diff)
else:
    print("You owe big brother")
    print(diff)




