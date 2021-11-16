from hx711 import HX711 

def Read_Voltage(samples):
    try:
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
            print(reading)

        
            
    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

def Voltage_to_Weight(voltage):

    A = 418.9713
    B = 127892.9

   
    return (voltage-B)/A


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
    import sys
    sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
    from crontab import CronTab
    
    cron = CronTab(user = True)
    job = cron.new(command = "python3 /home/pi/Senior-Design-Final/New_Design/Background_Feed_Now.py", comment = str(calories))
    
    job.minute.on(minute)
    job.hour.on(hour)
    job.day.every
    cron.write()

def setWeighing():
    print('hit')
    
    cron = CronTab(user = True)
    job = cron.new(command = "sudo python3 /home/pi/Senior-Design-Final/New_Design/Weigh.py", comment = "weigh")
    
    job.minute.every(1)
    cron.write()

def clearFeedings():
    from crontab import CronTab
    cron = CronTab(user = True)
    for job in cron:
        if str(job.comment) != "weigh":
            cron.remove(job)
    cron.write()