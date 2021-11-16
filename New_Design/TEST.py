from datetime import datetime
import croniter
from cron_descriptor import ExpressionDescriptor
from crontab import CronTab

# job = "1 5 * * *"

# print(ExpressionDescriptor(job))

cron = CronTab(user = True)

for job in cron:
    print(job)