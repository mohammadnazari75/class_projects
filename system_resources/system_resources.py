import os

command = os.popen('uptime')
output = command.read()

list = (output.strip()).split()
cpuload_5s = (list[7].split(","))[0]
cpuload_5m = (list[8].split(","))[0]
cpuload_15m = list[9]

print("\n===================================")
print(f'CPU Load Average:\n\nIn 5 Seconds:  {cpuload_5s}\nIn 5 Minutes:  {cpuload_5m}\nIn 15 Minutes: {cpuload_15m}')
print("===================================")

command_mem = os.popen('top -n 1')
line_to_read = [3]

for position, line in enumerate(command_mem):
    if position in line_to_read:
        mem = line

list_in_mem = (mem.strip()).split()
total_mem = list_in_mem[3]
used_mem = list_in_mem[7]
free_mem = list_in_mem[5]
mem_usage = (float(used_mem)*100)/float(total_mem)

print(f'Memory Usage:\n\nTotal Memory: {total_mem}\nUsed Memory:  {used_mem}\nFree Memory:  {free_mem}\nMemory Usage Percent: {int(mem_usage)}%')
print("===================================")

command_disk = os.popen('df -h')
line_to_read = [3]

for position, line in enumerate(command_disk):
    if position in line_to_read:
        disk = line

list_in_disk = (disk.strip()).split()
disk_name = list_in_disk[0]
disk_total = list_in_disk[1]
disk_used = list_in_disk[2]
disk_free = list_in_disk[3]
disk_usage = list_in_disk[4]

print(f'Disk Usage:\n\nDisk Name: {disk_name}\nTotal Disk Size: {disk_total}\nUsed Disk:\t {disk_used}\nFree Disk:\t {disk_free}\nDisk Usage Percent: {disk_usage}')
print("===================================")

command_net = os.popen('cat /proc/net/dev')
line_to_read = [3]

for position, line in enumerate(command_net):
    if position in line_to_read:
        net = line

list_in_net = (net.strip()).split()
net_name = (list_in_net[0].split(':'))[0]
net_rb = list_in_net[1]
net_rp = list_in_net[2]
net_tb = list_in_net[9]
net_tp = list_in_net[10]

print(f'Network Usage:\n\nNetwork Interface: {net_name}\nReceive Bytes:   {net_rb}\nReceive Packets: {net_rp}\nTransmit Bytes:  {net_tb}\nTransmit Packets: {net_tp}')
print("===================================\n")


