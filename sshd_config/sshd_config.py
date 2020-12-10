import os
from pyutil import filereplace

def sshd_config_mgr():

    user_req = input("\nWelcome to sshd_config manager:\n   [1] Operational Config\n   [2] Config Change\n    >:")
    if user_req == '1':
        with open ('sshd_config' , 'r') as openfile:
            for line in openfile:
                print(line)
    elif user_req == '2':
        oper_conf = input("\nEnter your operational config:\t")
        user_conf = input("Enter your new config:\t")
        filereplace('sshd_config', oper_conf, user_conf)
        os.system('sudo systemctl restart sshd')
    else:
        print("Invalid Input")

sshd_config_mgr()