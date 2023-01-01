import os
from rich.table import Table
from rich.console import Console
from CONF import Regex_Parser
import  concurrent.futures as cf
console = Console()

# set path too look for show outputs
os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_3/venv/SHOW")
reg = Regex_Parser()

# Parse show version
table = Table(title="\nSHOW VERSION",title_justify="center",title_style="bold",header_style="bold")
table.add_column("Hostname",justify="left",style="green")
table.add_column("Uptime",justify="left",style="green")
table.add_column("Serial Number",justify="left",style="green")
table.add_column("IOS",justify="left",style="green")
temp = []
for files in os.listdir():
    if "version" in files:
        temp.append(files)

for file in temp:
    with cf.ThreadPoolExecutor() as executor:
        version_out = [executor.submit(reg.version,file)]
        for f in cf.as_completed(version_out):
            table.add_row(f.result()[0],f.result()[1],f.result()[2],f.result()[3])
console.print(table,style="bold")

# Parse show run
temp.clear()
table = Table(title="\nSHOW RUN FOR INTERFACES",title_justify="center",title_style="bold",header_style="bold")
table.add_column("Hostname",justify="left",style="green")
table.add_column("Interface",justify="left",style="green")
table.add_column("IP address and its Subnet",justify="left",style="green")

for files in os.listdir():
    if "run" in files:
        temp.append(files)

for file in temp:
    with cf.ThreadPoolExecutor() as executor:
        run_out = [executor.submit(reg.run_interface,file)]
        for f in cf.as_completed(run_out):
            for int_name in f.result()[1]:
                host_name = f.result()[0]
                int_ip = f.result()[1][int_name]
                # console.print(f"{host_name} {name} {int_ip}")
                table.add_row(host_name,int_name,int_ip)
            table.add_section()

console.print(table,style="bold")

# Parse show ip int brief
temp.clear()
table = Table(title="\nSHOW IP INTERFACES BRIEF",title_justify="center",title_style="bold",header_style="bold")
table.add_column("Hostname",justify="left",style="green")
table.add_column("Interface",justify="left",style="green")
table.add_column("Interface IP",justify="left",style="green")
table.add_column("State",justify="left",style="green")

for files in os.listdir():
    if "interfaces" in files:
        temp.append(files)

for file in temp:
    with cf.ThreadPoolExecutor() as executor:
        brief_out = [executor.submit(reg.interface_brief,file)]
        for f in cf.as_completed(brief_out):
            int_name = f.result()[0]
            for interface,ip,state in f.result()[1]:
                table.add_row(int_name,interface,ip,state)
            table.add_section()
console.print(table,style="bold")








