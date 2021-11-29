import time
import RPi.GPIO as GPIO
from crontab import CronTab

t = time.localtime()
curHr = int(time.strftime('%H',t))
curMin = int(time.strftime('%M',t))

cron = CronTab(user = True)
for job in cron: 
    if job.comment != 'weigh':
        if (job.minute) == curMin and (job.hour) == curHr:
            calories = int(job.comment)
            break

feedtime = (float(calories) + 12.13)/22.277

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)

GPIO.output(38,1)
time.sleep(5)
# time.sleep(feedtime)
GPIO.output(38,0)
    
GPIO.cleanup()

python3 /home/pi/Senior-Design-FInal/New_Design/Feeding_Program.py