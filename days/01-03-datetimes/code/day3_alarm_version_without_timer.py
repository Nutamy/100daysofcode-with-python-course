from datetime import datetime, timedelta
from datetime import date
import time

# Вводим интервал через который сработает будильник
inputed_time = float(input("after how many minutes would you like to be reminded about the meeting, chef?"))

#Вычленяем из интервала минуты
minutes_input = int(inputed_time)

#Вычленяем из интервала секунда
seconds_input = int((inputed_time-minutes_input)*60)

#Формируем дельту
delta_min = timedelta(minutes=minutes_input, seconds=seconds_input)

#Засекаем точку отсчета
start_point = datetime.today()

#Прибавляем к текущему времени дельту
finish_point = start_point + delta_min

#Вычисляем интервал до будильника в секундах
timer = minutes_input*60+seconds_input
timer_triger = 0
print("start_point: ", start_point)
print("finish_point: ", finish_point)
print("You can relax. You have {} seconds to prepare".format(timer))
while timer_triger == 0:
    if (int(finish_point.minute) == int(datetime.today().minute)) and (int(finish_point.second) == int(datetime.today().second)):
        print("Chef, it is time to go to the meeting")
        timer_triger = 1
       
    else:
        time.sleep(1)
        '''if timer >1:
            print("You can relax. It is {} seconds left".format(timer))
        else:
            print("You can relax. It is {} second left".format(timer))
        timer -= 1'''

print("finish_point.minute: ", finish_point.minute)
print("datetime.today.minute: ", datetime.today().minute)
print("finish_point.second: ", finish_point.second)
print("datetime.today.second: ", datetime.today().second)
print("finish_point: ", finish_point)
print("datetime.today: ", datetime.today())
    
