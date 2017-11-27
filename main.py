from HarvestBalanceCalculator import DateStructure, WorkPeriod
from config.loader import load_configuration_file

config = load_configuration_file('config.json')

begin_date = DateStructure(config["beginDate"])
end_date = DateStructure(config["endDate"])

harvestPeriod = WorkPeriod(begin_date, end_date)

total_worked_time = harvestPeriod.get_total_number_of_worked_hours()
total_should_of_worked_time = harvestPeriod.get_total_should_of_worked_time()

diff = total_worked_time - total_should_of_worked_time

print("")

if diff > 0:
    print("You have some over time")
    print(diff)
else:
    print("You owe big brother")
    print(diff)




