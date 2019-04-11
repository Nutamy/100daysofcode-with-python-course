from datetime import datetime, timedelta
from datetime import date
import time

# Вводим интервал через который сработает будильник
inputed_time = float(input("after how many minutes would you like to be reminded about the meeting, chef?"))

#Вычленяем из интервала минуты
minutes_input = int(inputed_time)

#Вычленяем из интервала секунды
seconds_input = int((inputed_time-minutes_input)*60)

#Формируем дельту в секундах
delta_seconds = minutes_input*60+seconds_input
print("It is {}".format(datetime.today()))
print("We have {} seconds to prepare".format(delta_seconds))

timer_triger = 0
while timer_triger == 0:
    print("You can relax")
    time.sleep(delta_seconds)
    timer_triger = 1
print("Chef, it is time to go to the meeting")
print("It is {} Let's GO!".format(datetime.today()))
