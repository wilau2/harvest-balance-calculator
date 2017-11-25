import calendar

from timeUtils import get_number_of_weeks_between_dates
from harvestApi import HarvestApi


def get_full_weeks_worked_time_entries(a_monday, a_sunday):

    harvest_api = HarvestApi()

    print("The harvest api will be called with these parameters:")
    if a_monday.weekday() != calendar.MONDAY:
        raise RuntimeError('first param should be a monday')

    if a_sunday.weekday() != calendar.SUNDAY:
        raise RuntimeError('second param should be a sunday')

    if a_monday > a_sunday:
        raise RuntimeError('a_monday should be before a_sunday')

    return harvest_api.get_user_time_entries(a_monday, a_sunday)


def get_total_number_of_worked_hours(a_monday, a_sunday):
    time_entries = get_full_weeks_worked_time_entries(a_monday, a_sunday)
    total_worked_time = 0
    for time_entry in time_entries:
        total_worked_time += time_entry["hours"]
    return total_worked_time


def get_number_of_weeks_worked(begin_date, end_date):
    return get_number_of_weeks_between_dates(begin_date, end_date) + 1
