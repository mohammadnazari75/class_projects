import os

command = os.popen('which docker')
output = command.read()

if output == "/usr/bin/docker":
    print("\nDocker has been installed")
else:
    print("\nDocker is not installed in this host")
#
#import subprocess
#process1 = subprocess.Popen(['which', 'docker'],
#                     stdout=subprocess.PIPE, 
#                     stderr=subprocess.PIPE,
#                     universal_newlines=True)
#output = process1.stdout.read()
#print(output)
#if output == "/usr/bin/docker":
#    print("\nDocker has been installed")
#    process2 = subprocess.Popen(['docker', '-v'],
#                     stdout=subprocess.PIPE, 
#                     stderr=subprocess.PIPE,
#                     universal_newlines=True)
#    output = process2.stdout.read()
#    print(output)
#else:
#    print("\nDocker is not installed in this host")    