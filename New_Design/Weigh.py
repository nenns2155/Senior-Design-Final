from Backend import Read_Voltage, Voltage_to_Weight
import time
import csv

t1 = time.time()
w = Read_Voltage(20)
t2 = time.time()
t = (t1 + t2)/2

with open('weights.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([t,w])