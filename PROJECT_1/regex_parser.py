from myconflib import regex_version,regex_show_run,regex_ip_route
from rich.console import Console
from rich.table import Table
import os


console = Console()
# show version

table = Table(title="Extract from show Version in MAIN".title())

# get a file name
for file in os.listdir():
    if "version" in file:
        file_name = file
result = regex_version(file_name)

# Created table
table.add_column("Box Detail",justify="left",style="magenta")
table.add_column("Box Values",justify="left",style="magenta")
table.add_row("Uptime",result[1])
table.add_row("Board ID",result[2])
console.print(table,style="cyan")

# show run
table = Table(title="Extract from show run in MAIN".title())

# get a file name
for file in os.listdir():
    if "run" in file:
        file_name = file

result = regex_show_run(file_name)
hostname,domain,d_inf_ip = result

# Table added for hostname and domain name
table.add_column("Device Attributes",justify="left",style="magenta")
table.add_column("Values",justify="left",style="magenta")
table.add_row("Hostname",hostname)
table.add_row("Domain name",domain)
console.print(table,style="cyan")

# Table added for interface name and IP details
table = Table(title="Interfaces Details".title())
table.add_column("Interface",justify="left",style="magenta")
table.add_column("IP and its Subnet",justify="left",style="magenta")

for inf,ip in d_inf_ip.items():
    table.add_row(inf,ip)
    # print(f"Interface is {inf.ljust(22)} : {ip.rjust(30)}")
console.print(table,style="cyan")

# show ip route
table = Table(title="Extract from ip route".title())
# get a file name
for file in os.listdir():
    if "route" in file:
        file_name = file

result = regex_ip_route(file_name)
table.add_column("Subnet",justify="left",style="magenta")
table.add_column("Next Hop",justify="left",style="magenta")

for subnet,out_inf in result.items():
    table.add_row(subnet,out_inf)
    # print(f"Subnet is {subnet.ljust(17)} : Outgoing Interfca is {out_inf.rjust(25)}")
console.print(table,style="cyan")    
