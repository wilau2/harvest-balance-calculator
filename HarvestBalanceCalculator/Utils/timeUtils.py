from datetime import timedelta


def get_number_of_weeks_between_dates(begin_date, end_date):
    monday1 = (begin_date - timedelta(days=begin_date.weekday()))
    monday2 = (end_date - timedelta(days=end_date.weekday()))
    return (monday2 - monday1).days / 7
