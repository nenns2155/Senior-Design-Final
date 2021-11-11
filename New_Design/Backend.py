from hx711 import HX711
import RPi.GPIO as GPIO  # import GPIO

def Read_Voltage(samples):
    try:
        GPIO.setmode(GPIO.BOARD) # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=36, pd_sck_pin=35)

        lastreading = hx._read()
        count = 0
        sum = 0
        while True:
            reading = hx._read()
            if reading == -1:
                lastreading = reading
                pass
            elif count == samples:
                return Voltage_to_Weight(sum/samples)
            elif reading < 0:
                pass
            elif reading == False:
                pass
            elif abs(lastreading/reading) > 1.25 or abs(lastreading/reading) < .75:
                pass
            else:
                sum = sum + reading
                count = count + 1
            
            lastreading = reading    
            
    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

def Voltage_to_Weight(voltage):

    A = 190033
    B = 262378.645
    C = 256951.0917

    return voltage


# def Calibration():

#     print("I should be doing a calibration")
    # weight = []
    # voltage = []

    # for i in range(0, 42, 2):
    #     i=i/4
    #     input("Press enter when {} lbs are on the scale.".format(i))
    #     weight.append(i)
    #     voltagepoint = Read_Voltage(20)
    #     voltage.append(voltagepoint)
    #     print("Weight equals:", i)
    #     print("Voltage equals:",voltagepoint)


    # [A,B,C] = np.polyfit(weight, voltage, 2)

    # print('A equals:', A)
    # print('B equals:', B)
    # print('C equals:', C)



def setFeeding(hour, minute, calories):

    print(hour)
    print(minute)
    print(calories)

    # import sys
    # sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
    
    # # from crontab import CronTab
    
    # cron = CronTab(user = True)
    # job = cron.new(command = "print( 'Hit')", comment = str(calories))
    
    # job.minute.on(minute)
    # job.hour.on(hour)
    # job.dow.every(d)
    # cron.write()