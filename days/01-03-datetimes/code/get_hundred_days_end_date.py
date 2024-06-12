from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    hundred_days_end_date = start_100days + timedelta(days=100)
    return hundred_days_end_date

print(get_hundred_days_end_date())
