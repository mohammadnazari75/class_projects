import os

command = os.popen('uptime')
output = command.read()

list = (output.strip()).split()
uptime = (list[2].split(","))[0]

if uptime < '0:10':
    print("\nSystem has been restarted recently")
else:
    print("\nSystem Uptime:" , uptime, "\n")