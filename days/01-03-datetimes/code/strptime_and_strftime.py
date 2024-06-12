from datetime import datetime
from datetime import date
import time

THIS_YEAR = 2019


def years_ago(date):
    received_date = datetime.strptime(date, "%d %b, %Y")
    delta = THIS_YEAR - int(received_date.year)
    return delta

test_1_1 = years_ago('8 Aug, 2015')
test_1_2 = years_ago('6 Sep, 2014')
test_1_3 = years_ago('1 Oct, 2010')
test_1_4 = years_ago('31 Dec, 1958')

print("test_1_1 = 8 Aug, 2015: ", test_1_1)
print("test_1_2 = 6 Sep, 2014: ", test_1_2)
print("test_1_3 = 1 Oct, 2010: ", test_1_3)
print("test_1_4 = 31 Dec, 1958: ", test_1_4)

def convert_eu_to_us_date(date):
    received_date = datetime.strptime(date, "%d/%m/%Y")
    american_date = received_date.strftime("%m/%d/%Y")
    return american_date

test_2_1 = convert_eu_to_us_date('11/03/2002')
test_2_2 = convert_eu_to_us_date('18/04/2008')
test_2_3 = convert_eu_to_us_date('12/12/2014')
test_2_4 = convert_eu_to_us_date('1/3/2004')
print("test_2_1 = 11/03/2002: ", test_2_1)
print("test_2_2 = 18/04/2008: ", test_2_2)
print("test_2_3 = 12/12/2014: ", test_2_3)
print("test_2_4 = 1/3/2004: ", test_2_4)
