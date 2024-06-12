from datetime import datetime
from datetime import date

my_birthday = date(1985, 7, 8)
print("Hello everyone!\nI was born on 8 July, 1985. \nI have lived ", (date.today() - my_birthday).days, " days")
print("Let's see how lond have you lived.")
your_year = int(input("\nType the year you were born: "))
your_month = int(input("\nJanuary - 1\nFebruary - 2\nMarch - 3\nApril - 4\nMay - 5\nJune - 6\nJuly - 7\nAugust - 8\nSeptember - 9\nOctober - 10\nNovember - 11\nDecember - 12\n\nType the month you were born: "))
your_day = int(input("Type the day you were born: "))
your_birthday = date(your_year, your_month, your_day)
print("You have lived ", (date.today() - your_birthday).days, " days")
