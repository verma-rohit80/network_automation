"""
1. Scans show version and print IOS version, UP time and board ID
2. Scans show run and print hostname, Domain name and Interface name with IP address
"""
import re
from  rich import print,box
from rich.table import Table
from rich.console import Console

console = Console()
def regex_version(file_name):
    with open(file_name) as f:
        f_ver = f.read()
    
    # Capture COde Version
    version_compile = re.compile(r"""(?<=Version)\s(.+),  # Capture  anything after Version but before ,
                                """,re.MULTILINE | re.VERBOSE)
    result_version = version_compile.search(f_ver)
   

    # Capture Uptime
    version_uptime = re.compile(r"""(?<=uptime\sis)\s(.+) # capture  anything after Version but before \n
                                """,re.MULTILINE | re.X)
    result_uptime = version_uptime.search(f_ver)


    # Capture boad ID
    version_board_id = re.compile(r"""(?<=ID)\s(\w+)      #  Capture everthing after ID
                                  """,re.MULTILINE | re.X)
    result_board_id = version_board_id.search(f_ver)
   
    return [result_version.group(1),result_uptime.group(1),result_board_id.group(1)]
                                
    

def regex_show_run(file_name):
    with open(file_name) as f:
        f_run = f.read()

    # Capture Hostname
    run_hostname = re.compile(r"(?<=hostname\s)(\w.+)",re.MULTILINE)
    result_hostname = run_hostname.search(f_run)

    # Capture domain name
    run_domain = re.compile(r"(?<=domain\sname)\s(\w.+)",re.MULTILINE)
    result_domain = run_domain.search(f_run)
    # print(result_domain.group(1))

    # Dict of Interface name : IP address
    ip_addr = dict()
    run_ip = re.compile(r"""interface\s(\w.+)\n   # apture anything after interface till \n
                            (?:.+\n)?             # If line exist , ignore it
                            \s?ip\saddress\s(.+)  # space or no space followed bp ip address and capture everything after IP addr
                            """,re.MULTILINE | re.VERBOSE)
    
    result_ip = run_ip.findall(f_run) 
    for _ in result_ip:
        interface,ip_address = _
        ip_addr[interface] = ip_address
    
    return result_hostname.group(1),result_domain.group(1),ip_addr


def regex_ip_route(file_name):
    ip_route = dict()
    with open(file_name) as f:
        f_route = f.read()
    d_route = dict()
    route_hop = re.compile(r"^C\s+(.+) is.+(Gig.*)",re.MULTILINE)
    result_hop = route_hop.findall(f_route)
    
    for _ in result_hop:
        subnet,out_inf = _
        ip_route[subnet] = out_inf
    
    return ip_route

# show version
table = Table(title="Extract from show Version".title())
file_name = "2022-11-08__02__192.168.1.11__show version.txt"
result = regex_version(file_name)
# Created table
table.add_column("Box Detail",justify="left",style="magenta")
table.add_column("Box Values",justify="left",style="magenta")
table.add_row("Uptime",result[1])
table.add_row("Board ID",result[2])
console.print(table,style="cyan")

# show run
table = Table(title="Extract from show run".title())
file_name = "2022-11-08__01__192.168.1.11__show run.txt"
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
file_name = "2022-11-08__03__192.168.1.11__show ip route.txt"
result = regex_ip_route(file_name)
table.add_column("Subnet",justify="left",style="magenta")
table.add_column("Next Hop",justify="left",style="magenta")

for subnet,out_inf in result.items():
    table.add_row(subnet,out_inf)
    # print(f"Subnet is {subnet.ljust(17)} : Outgoing Interfca is {out_inf.rjust(25)}")
console.print(table,style="cyan")    

