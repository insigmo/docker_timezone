import json
from datetime import datetime

from pytz import timezone, common_timezones

timezones = {}

for tz in common_timezones:
    now = datetime.now(timezone(tz))
    tz_hour = int(now.strftime("%z")[:3])
    timezones.update({str(tz_hour): tz})

with open('timezone.json', 'w') as f:
    json.dump(timezones, f, sort_keys=True, indent=4)
