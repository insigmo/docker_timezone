import argparse
import json
import os
import time
from datetime import datetime
from subprocess import Popen


CURRENT_DIR = os.path.dirname(__file__)
TIMEZONE_PATH = os.path.join(CURRENT_DIR, 'timezone.json')

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", help="hour appropriate for timezone")
parser.add_argument("-n", "--docker-name", help="docker container name or id")
args = parser.parse_args()

hour = int(args.time)
assert hour, 'You have to set parameters --time: "{}""'.format(args.time)
assert 0 <= hour <= 24, 'Time has to set from 0 to 24. --time: "{}""'.format(args.time)
assert args.docker_name, 'You have to set parameters --docker-name: "{}"'.format(args.docker_name)


with open(TIMEZONE_PATH, 'r') as f:
    timezones = json.load(f)


right_offset = int(datetime.now().strftime("%H")) - hour
offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
offset //= -3600 - right_offset


cmd = 'docker exec -d {} bash -c "timedatectl set-timezone {}"'.format(args.docker_name, timezones[str(offset)])
Popen(cmd, shell=True)
