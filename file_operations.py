from  paramiko import client,ssh_exception
from  getpass import getpass 
import datetime
import time
import sys
import os

def cisco_cmd_push(hostname,commands):
    try:
        device_ssh = client.SSHClient()
        device_ssh.set_missing_host_key_policy(client.AutoAddPolicy)
        device_ssh.connect(hostname=hostname,
                            port = 22,
                            username = username,
                            password = password,
                            look_for_keys=False)

        print("Connection established successfully")

        now = datetime.datetime.now().replace(microsecond=0)
        now = str(now).split()[0]
        file_name = f"{now}:{hostname}.txt"
        print(file_name)
        device_access = device_ssh.invoke_shell()
        device_access.send("terminal length 0\n")
        # Push config one cmd at a time
        for cmd in commands:
            device_access.send(f"{cmd}")
            time.sleep(1)
            outout = device_access.recv(65535)
            print(outout.decode(),end = " ")
        # Push show run in a text file
        with open(file_name,"w") as f:
            device_access.send("show run\n")
            time.sleep(10)
            output = device_access.recv(65535)
            f.write(output.decode())
            device_ssh.close()
    # Handling Authentication an wrong hostnames exceptions
    except ssh_exception.AuthenticationException:
        print("Correct the password")
    except ssh_exception.NoValidConnectionsError:
        print("Hostname IP is Incorrect")
    



# Read from a file al the commands that need to be pushed
with open("config.txt","r") as cfg:
    config = cfg.readlines()
hostnames = ["192.168.1.11","192.168.1.12"]
for hostname in hostnames:
    username = input("Please enter an username ? ")
    password = getpass(f"Please enter password for {username} ?  ")
    # commands = ["config t","int loop 99","ip address 99.99.99.99 255.255.255.255","end"]
    cisco_cmd_push(hostname,config)
 