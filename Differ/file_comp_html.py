from itertools import count
import paramiko
from paramiko import client,ssh_exception
import datetime
import time
import os
import difflib
import webbrowser

def config_pull(hostname,commands):
    try:
        now = datetime.datetime.now().replace(microsecond=0)
        device_ssh = client.SSHClient()
        device_ssh.set_missing_host_key_policy(client.AutoAddPolicy)
        device_ssh.connect(hostname = hostname,
                            port = 22,
                            username = username,
                            password = password,
                            look_for_keys=False)
        print("Connection established")
        os.chdir("Differ")
        f_path = os.getcwd()
        device_access = device_ssh.invoke_shell()
        device_access.send("terminal length 0\n")
        time.sleep(4)
        for cmd in enumerate(commands,start=1):
            file_name = f"{str(now).replace(' ',':')}__{str(cmd[0]).zfill(2)}__{hostname}.txt"
            file_name = f_path + "/" + file_name
            with open(file_name,"w") as f_write:
                device_access.send(f"{cmd[1]}")
                time.sleep(10)
                output = device_access.recv(65535)
                f_write.write(output.decode())
                device_access.close()
                print("Disconnected from the device")
        # Comparison from ref file to current pulled config
        with open("r1_ref.txt") as ref_file:
            ref = ref_file.readlines()
        with open(file_name) as curr_file:
            curr = curr_file.readlines()
        
        # Write to a file and open in a browser
        compare_files = difflib.HtmlDiff().make_file(fromlines=ref,tolines=curr)
        with open("diff.html","w") as diff_file:
            diff_file.write(compare_files)
        webbrowser.open_new_tab("diff.html")
    except ssh_exception.AuthenticationException:
        print("Authentication error")
    except ssh_exception.NoValidConnectionsError:
        print("IP address of host is Incorrect")

path = "/home/rohit/Documents/python/Udemy/para_miko/para_virtual/Differ/config_pull.txt"
with open(path) as f_pull:
    f_read = f_pull.readlines()
    # for cmd in enumerate(f_read):
    #      print(cmd[1])

hostname = "192.168.1.11"
username = "admin"
password = "cisco"
config_pull(hostname,f_read)

