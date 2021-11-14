from Backend import Read_Voltage, Voltage_to_Weight
import time
import csv

import RPi.GPIO as GPIO  # import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

GPIO.output(32,1)


t1 = time.time()
w = Read_Voltage(20) 
t2 = time.time()
t = (t1 + t2)/2

with open('/home/pi/Senior-Design-Final/New_Design/weights.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([t,w])

GPIO.cleanup()