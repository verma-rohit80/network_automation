from http import client
from  paramiko import client,ssh_exception
from  getpass import getpass 
import time
import sys



def cisco_cmd_execution(hostname,commands):
    try:
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
        ssh_client.connect(hostname = hostname,
                            port = 22,
                            username = username,
                            password = password,
                            look_for_keys=False,
                            )
        print("Connected Sucessfully")

        # Execute a command 
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n") 
        for cmd in commands:
            device_access.send(f"{cmd}\n")
            time.sleep(1)
            output = device_access.recv(65535)
            print(output.decode(),end="")

        device_access.send("show run int loop1000\n")
        time.sleep(1)
        output = device_access.recv(65535)
        print(output.decode(),end="")
        ssh_client.close()
    except ssh_exception.AuthenticationException:
        print(" Autentication Failed ")
    except ssh_exception.NoValidConnectionsError:
        print("Check hostname IP address")
        

hostnames = ["192.168.1.11","192.168.1.12"]
for hostname in hostnames:
    username = input(f"Please enter username for {hostname}? ")
    password = getpass(f"\U0001F511 Enter password of user {username}: ") or "cisco"
    commands = ["config t"," int loop 1000","ip address 100.100.100.100 255.255.255.255","end"]
    cisco_cmd_execution(hostname,commands)