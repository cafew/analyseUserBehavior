import subprocess
import sys

COMMANDS = [
    "python /app/datax/bin/datax.py /app/datax/bin/newHouseLog.json",
    "python /app/datax/bin/datax.py /app/datax/bin/newHouse.json",
    "python /app/datax/bin/datax.py /app/datax/bin/phoneDevice.json"]


def action(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in p.stdout:
        print(line.decode('utf-8'))
    p.wait()
    print(p.returncode)


def begin():
    for command in COMMANDS:
        print(command)
        action(command)


if __name__ == '__main__':
    for command in COMMANDS:
        action(command)