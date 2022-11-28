from regex_base import Regex
import os
import concurrent.futures as cf
from rich.console import Console
from rich.table import Table

# Setting the environment
os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/CISCO_OUTPUTS")
regex_object = Regex()
console = Console()

#  Working with show version
table = Table(title="extract from show version".upper(),header_style="bold",title_style="bold")
filenames = []
for file in os.listdir():
    if "version" in file:
        filename = file
        filenames.append(filename)

table.add_column("Box Detail",justify="left",style="green")
table.add_column("Box Values",justify="left",style="green")

for file in filenames:
    hostname = file.split("_")[0]
    with cf.ThreadPoolExecutor() as executor:
        ver = [executor.submit(regex_object.regex_version,file)]
        for f in cf.as_completed(ver):
            table.add_row("Hostname",hostname)
            table.add_row("Version",f.result()[0])
            table.add_row("System Image FIle",f.result()[1])
            table.add_row("Uptime",f.result()[2])
            table.add_row("Board ID",f.result()[3])
            table.add_section()
console.print(table,style="Cyan")
# End of show version

# Working with show run for hostname and domain name
filenames = []
for file in os.listdir():
    if "run" in file:
        filenames.append(file)

table = Table(title="extract from show run for attributes".upper(),title_style="bold",header_style="bold",title_justify="center")
table.add_column("Device",justify="left",style="green")
table.add_column("Values",justify="left",style="green")

for file in filenames:
    with cf.ThreadPoolExecutor() as executor:
        run = [executor.submit(regex_object.regex_run,file)]
        for f in cf.as_completed(run):
            table.add_row("Hostname",f.result()[0])
            table.add_row("Domain Name",f.result()[1])
            table.add_section()
console.print(table,style="cyan")
# End of working with show run for hostname and domain name

# Working with show run for interface details
filenames = []
for file in os.listdir():
    if "run" in file:
        filenames.append(file)

table = Table(title="Extract froms show run for interface and its subnet details".upper(),title_style="bold",header_style="bold",title_justify="center")
table.add_column("Hostname",justify="left",style="green")
table.add_column("Interface",justify="left",style="green")
table.add_column("IP and its Subnet",justify="left",style="green")

for file in filenames:
    with cf.ThreadPoolExecutor() as executor:
        run = [executor.submit(regex_object.regex_run_interfaces,file)]  # returns dict of interface with IP and mask
        hostname = [executor.submit(regex_object.regex_run,file)]        # returns (hostname,domainname) in tuple
        for f in zip(cf.as_completed(run),cf.as_completed(hostname)):    # iterate through zip of dict and tuple
            interface_details = f[0].result()                            # f[0] is dict of interface name: IP details
            host = f[1].result()[0]                                      # f[1] is a tuple of (hostname,domain) and slice [0]
            for key,value in interface_details.items():
                table.add_row(host,key,value)
            table.add_section()
console.print(table,style="cyan")
# End of working with show run for interface details

# Working with show ip route for destination , next hop and outgoing interface
filenames = []
for file in os.listdir():
    if "route" in file:
        filenames.append(file)
table = Table(title="extract from ip route".upper(),title_style="bold",title_justify="center",header_style="bold")
table.add_column("Subnet",justify="left",style="green")
table.add_column("Outgoing Interface",justify="left",style="green")
table.add_column("Route Type",justify="left",style="green")

for file in filenames:
    with cf.ThreadPoolExecutor() as executor:
        route = [executor.submit(regex_object.regex_route,file)]
        for f in cf.as_completed(route):
            for route_tuple in f.result():   # Example ('C', '155.1.45.0/24', 'GigabitEthernet0/1.45')
                table.add_row(route_tuple[1],route_tuple[2],route_tuple[0])
            table.add_section()
console.print(table,style="cyan")
# Fin Working with show ip route for destination , next hop and outgoing interface