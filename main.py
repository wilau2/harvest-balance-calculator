from dateutil.parser import parse

from banner import print_banner
from configurationLoader import load_configuration_file
from domain import get_number_of_weeks_worked, get_total_number_of_worked_hours
from timeUtils import get_monday_from_week_including_date, get_sunday_from_week_including_date, get_day_name_of_week

config = load_configuration_file('config.json')

print_banner()


begin_date = parse(config["beginDate"]).date()
print("\nThe configuration beginning date is: " + begin_date.isoformat() + " " + get_day_name_of_week(begin_date))

end_date = parse(config["endDate"]).date()
print("\nThe configuration ending date is: " + end_date.isoformat() + " " + get_day_name_of_week(begin_date))

beginning_monday = get_monday_from_week_including_date(begin_date)
ending_sunday = get_sunday_from_week_including_date(end_date)

total_worked_time = get_total_number_of_worked_hours(beginning_monday, ending_sunday)

number_of_weeks_worked = get_number_of_weeks_worked(beginning_monday, ending_sunday)

total_should_of_worked_time = number_of_weeks_worked * float(config["hoursPerWeek"])

diff = total_worked_time - total_should_of_worked_time

print("")

if diff > 0:
    print("You have some over time")
    print(diff)
else:
    print("You owe big brother")
    print(diff)




