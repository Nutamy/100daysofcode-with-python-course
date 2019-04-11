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

#Создаём цикл для отсчета секунд указав в рандже интервал до будильника в секундах
for step in range(minutes_input*60+seconds_input):
    #Если ещё не время (но эта строчка кажеться не работает)
    if finish_point is not datetime.today():
        if timer >1:
            print("You can relax. It is {} seconds left".format(timer))
        else:
            print("You can relax. It is {} second left".format(timer))
        timer -= 1
    time.sleep(1)
print("Chef, it is time to go to the meeting")
print("finish_point: ", finish_point)
print("datetime.today", datetime.today())
    
