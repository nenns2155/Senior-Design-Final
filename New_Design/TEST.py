from datetime import datetime
import croniter
from cron_descriptor import ExpressionDescriptor
from crontab import CronTab

job = "@Daily"

print(ExpressionDescriptor(job))
