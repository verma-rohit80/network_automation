from  paramiko import client,ssh_exception
from  getpass import getpass 
import time
import sys
import os

def cisco_cmd_push(hostname,commands):
    device_ssh = client.SSHClient()
    device_ssh.set_missing_host_key_policy(client.AutoAddPolicy)
    device_ssh.connect(hostname=hostname,
                        port = 22,
                        username = username,
                        password = password,
                        look_for_keys=False)

    print("Connection established successfully")
    device_access = device_ssh.invoke_shell()
    device_access.send("terminal length 0\n")
    for cmd in commands:
        device_access.send(f"{cmd}\n")
        time.sleep(1)
        outout = device_access.recv(65535)
        print(outout.decode(),end = " ")
    
    device_access.send("show run int loop 99\n")
    time.sleep(1)
    output = device_access.recv(65535)
    print(output.decode(),end = "")
    device_ssh.close()
    

hostnames = ["192.168.1.11","192.168.1.12"]
for hostname in hostnames:
    username = input("Please enter an username ? ")
    password = getpass(f"Please enter password for {username} ?  ")
    commands = ["config t","int loop 99","ip address 99.99.99.99 255.255.255.255","end"]
    cisco_cmd_push(hostname,commands)