
import re,pprint
from rich.table import Table
from rich.console import Console
console = Console()
table = Table(title="Interfaces With IPs")
inf = """
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         192.168.1.11    YES NVRAM  up                    up      
GigabitEthernet0/1         unassigned      YES NVRAM  up                    up      
GigabitEthernet0/1.13      155.1.13.1      YES NVRAM  up                    up      
GigabitEthernet0/1.100     169.254.100.1   YES NVRAM  up                    up      
GigabitEthernet0/1.146     155.1.146.1     YES NVRAM  up                    up      
GigabitEthernet0/2         unassigned      YES NVRAM  up                    up      
GigabitEthernet0/3         unassigned      YES NVRAM  up                    up      
Loopback0                  150.1.1.1       YES NVRAM  up                    up      
Tunnel0                    155.1.0.1       YES NVRAM  up                    up 
"""
t = re.compile(r"(\S+)\s+([\d\.]+)")
res = t.findall(inf)
table.add_column("Interfaces",justify="left",style="cyan")
table.add_column("IP Address",justify="left",style="cyan")

for item in res:
    inf,ip = item
    table.add_row(inf,ip)
console.print(table)

