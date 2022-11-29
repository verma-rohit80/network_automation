# file name : conf/base_main_config.py

from netmiko import ConnectHandler,exceptions
from dotenv import load_dotenv
import os

class Config_puller:

    def cisco_config_pull(self,**kwargs):
        self.IP = kwargs["host"]
        try:
            with ConnectHandler(**kwargs) as self.conn:
                print(f"started with Hostname {kwargs['host']}")
                self.connect_version()
                self.connect_run()
                self.connect_route()

        except exceptions.ConnectionException:
            print(f"{kwargs['host']} IP is not reachable")
        except exceptions.NetMikoAuthenticationException:
            print(f"{kwargs['host']}Authentication error")
        except exceptions.NetMikoTimeoutException:
            print(f"{kwargs['host']} SSH Timeout")

    def connect_version(self):
        filename = f"CISCO_SHOW/{self.IP}__show_version.txt"
        output = self.conn.send_command("show version")
        with open(filename,"w") as f:
            f.write(output)

    def connect_run(self):
        filename = f"CISCO_SHOW/{self.IP}__show_run.txt"
        output = self.conn.send_command("show run")
        with open(filename,"w") as f:
            f.write(output)

    def connect_route(self):
        filename = f"CISCO_SHOW/{self.IP}__show _ip_route.txt"
        output = self.conn.send_command("show ip route")
        with open(filename,"w") as f:
            f.write(output)
