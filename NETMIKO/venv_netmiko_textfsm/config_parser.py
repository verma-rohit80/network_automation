from conf import config_textfsm
import os
from rich.table import Table
from rich.console import Console
import  concurrent.futures as cf

object_parser = config_textfsm()
console = Console()
PATH = os.path.join(
    "/home","rohit","Documents","python","Udemy","para_miko","para_virtual","NETMIKO","venv_netmiko_textfsm","CISCO_SHOW"
)
# start show version
filenames = list()
template_file="cisco_ios_show_version.textfsm"
for file in os.listdir(PATH):
    if "version" in file:
        filenames.append(file)

table = Table(title="EXTRACT FROM SHOW VERSION",title_style="bold",header_style="bold")
table.add_column("Box Attributes",justify="left",style="green")
table.add_column("Box Values",justify="left",style="green")

for filename in filenames:
    with cf.ThreadPoolExecutor() as executor:
        output = [executor.submit(object_parser.textfsm_version,filename,template_file)]
        for f in cf.as_completed(output):
            for inner in f.result():
                table.add_row("Hostname",inner[2])
                table.add_row("Code Version",inner[0])
                table.add_row("Uptime",inner[3])
                table.add_row("IOS",inner[10])
                table.add_row("Serial Number",inner[12][0])
            table.add_section()
console.print(table)        
# FIN show version

# Start with show ip route
filenames = list()
template_file="cisco_ios_show_ip_route.textfsm"
for file in os.listdir(PATH):
    if "route" in file:
        filenames.append(file)
table = Table(title="EXTRACT FROM SHOW IP ROUTE",title_style="bold",header_style="bold")
table.add_column("HOstname",justify="left",style="green")
table.add_column("Type",justify="left",style="green")
table.add_column("Network",justify="left",style="green")
table.add_column("Subnet",justify="left",style="green")
table.add_column("AD",justify="left",style="green")
table.add_column("Cost",justify="left",style="green")
table.add_column("Next Hop",justify="left",style="green")
table.add_column("Outgoing Interface",justify="left",style="green")

for filename in filenames:
    hostname = filename.split("_")[0]
    with cf.ThreadPoolExecutor() as executor:
        output = [executor.submit(object_parser.textfsm_version,filename,template_file)]
        for f in cf.as_completed(output):
            for inner in f.result():
                table.add_row(hostname,inner[0],inner[2],inner[3],inner[4],inner[5],inner[6],inner[7])
            table.add_section()
            
console.print(table)



