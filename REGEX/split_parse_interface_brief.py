from rich.table import Table
from rich.console import Console
console = Console()
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

# Creatinbg tables
table = Table(title="Interfaces With IPs".title())
table.add_column("Interface Name",justify="left")
table.add_column("Interface IPs",justify="left")
interfaces = inf.splitlines()
int_slice = interfaces[2:]

# console.print(interfaces)
# console.print(int_slice)

for interface in int_slice:
    int_parse = interface.split()
    if "unassigned" not in int_parse:
        table.add_row(int_parse[0],int_parse[1])

console.print(table)