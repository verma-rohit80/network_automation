import paramiko
from paramiko import client,ssh_exception
import os,time,datetime



def pull_config(hostname,commands):
    print(hostname)
    try:
        # Get current datetime and extract date from it
        now = str(datetime.datetime.now().replace(microsecond=0)).split()[0]
        path = os.getcwd()

        # Config for SSH Connections
        device_ssh = client.SSHClient()
        device_ssh.set_missing_host_key_policy(client.AutoAddPolicy)
        device_ssh.connect(hostname=hostname,
                           port=22,
                           username=username,
                           password=password,
                           look_for_keys=False)
        print("Connection extablished")
        # Config to  invole sheel and push commands
        device_access = device_ssh.invoke_shell()
        for cmd in enumerate(commands,start=1):
            file_name = f"{now}__{str(cmd[0]).zfill(2)}__{hostname}__{cmd[1]}.txt"
            file_name = f"{path}/{file_name}"
            with open(file_name,"w") as f:
                device_access.send("terminal length 0\n")
                device_access.send(f"{cmd[1].strip()}\n")
                time.sleep(8)
                output = device_access.recv(65535)
                f.write(output.decode())
        device_access.close()
        print("Connection is closed")

    except ssh_exception.AuthenticationException:
        print("Password is Wrong")

    except ssh_exception.NoValidConnectionsError:
        print("Hostname is Wrong")

with open("hostname.txt") as f_hostnames:
    f_hostnames = f_hostnames.readlines()

with open("commands.txt") as f_commands:
    f_commands = f_commands.readlines()

for hostname in f_hostnames:
    hostname = hostname.strip()
    print(len(hostname))
    print(hostname)
    username = "admin"
    password = "cisco"
    pull_config(hostname,f_commands)

