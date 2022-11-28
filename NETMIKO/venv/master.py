import os,rich
from netmiko import ConnectHandler
from dotenv import load_dotenv

class Cisco:
    def __init__(self,**cisco_device):
        self.connect_version(cisco_device)
        self.connect_interface(cisco_device)
        self.connect_run(cisco_device)
        self.connect_route(cisco_device)
        
    
    def connect_version(self,cisco_device):
        with ConnectHandler(**cisco_device) as conn:
            output = conn.send_command("show version")
            hostname = cisco_device["host"]
            file_name = f"{hostname}__show_version"
            os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/CISCO_OUTPUTS")
            with open(file_name,"w") as f:
                f.write(output)


    def connect_interface(self,cisco_device):
        hostname = cisco_device["host"]
        file_name = f"{hostname}__show_interface_brief.txt"
        with ConnectHandler(**cisco_device) as conn:
            output = conn.send_command("show ip interface brief")
            os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/CISCO_OUTPUTS")
            with open(file_name,"w") as f:
                f.write(output)


    def connect_run(self,cisco_device):
        hostname = cisco_device["host"]
        file_name = f"{hostname}__show_run.txt"
        with ConnectHandler(**cisco_device) as conn:
            output = conn.send_command("show run")
            os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/CISCO_OUTPUTS")
            with open(file_name,"w") as f:
                f.write(output)
    
    def connect_route(self,cisco_device):
        hostname = cisco_device["host"]
        file_name = f"{hostname}__show_ip_route.txt"
        with ConnectHandler(**cisco_device) as conn:
            output = conn.send_command("show ip route")
            os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/CISCO_OUTPUTS")
            with open(file_name,"w") as f:
                f.write(output)



