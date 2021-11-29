def weigh():    
    from Backend import Read_Voltage, Voltage_to_Weight
    import time
    import csv

    import RPi.GPIO as GPIO  # import GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)

    GPIO.output(32,1)


    t= time.localtime()
    curHr = float(time.strftime('%H', t))
    curMin = float(time.strftime('%M', t))
    t = float(curHr+curMin/60)

    w = Read_Voltage(20) 

    with open('/home/pi/Senior-Design-Final/New_Design/weights.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([t,w])

    GPIO.cleanup()
    return w

if __name__ == "__main__":
    weigh()