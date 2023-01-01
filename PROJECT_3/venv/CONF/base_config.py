import rich,os
from netmiko import ConnectHandler,exceptions

class Cisco:
    def initialization(self,**devices):
        try:
            self.conn = ConnectHandler(**devices)
            self.hostname = devices["host"]
            set_path = f"/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_3/venv/SHOW"
            os.chdir(set_path)
            # rich.print(os.getcwd())
        except exceptions.NetMikoAuthenticationException:
            return (f"{devices['host']} has password issues")
            
        except exceptions.ConnectionException:
            return (f"{devices['host']} is not reachable")

        except exceptions.NetmikoTimeoutException:
            return (f"{devices['host']} ssh timeout")
                

    def sh_version(self):
        output = self.conn.send_command("show version")
        file_name = f"{self.hostname}__version"
        with open(file_name,"w") as f:
            f.write(output)
        self.connection_close()
        

    def route_ospf(self):
        output = self.conn.send_command("show ip route ospf")
        file_name = f"{self.hostname}__route_ospf"
        with open(file_name,"w") as f:
            f.write(output)
        self.connection_close()

    
    def interfaces(self):
        output = self.conn.send_command("show ip int brief")
        file_name = f"{self.hostname}__interfaces"
        with open(file_name,"w") as f:
            f.write(output)
        self.connection_close()
    def run(self):
        output = self.conn.send_command("show run")
        file_name = f"{self.hostname}__run"
        with open(file_name,"w") as f:
            f.write(output)
        self.connection_close()

    def connection_close(self):
        self.conn.disconnect()



device = {
    "device_type" : "cisco_ios",
    "host" : "192.168.1.11",
    "username" : "admin",
    "password" : "cisco"

}

cisco = Cisco()
excep = cisco.initialization(**device)
# if excep:
#     print(excep)
# else:
#     cisco.sh_version()