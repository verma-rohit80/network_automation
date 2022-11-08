"""
1. Scans show version and print IOS version, UP time and board ID
2. Scans show run and print hostname, Domain name and Interface name with IP address
"""
import re
from  rich import print
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
print("Extract from show Version")
file_name = "2022-11-08__02__192.168.1.11__show version.txt"
result = regex_version(file_name)
print(f"{'Version'.ljust(20)} : {result[0].rjust(len(result[2])+1)}")
print(f"{'Uptime is'.ljust(20)} : {result[1].rjust(len(result[2])+1)}")
print(f"{'Board ID is'.ljust(20)} : {result[2].rjust(len(result[2])+1)}")
print()

# show run
print("Extract from show run")
file_name = "2022-11-08__01__192.168.1.11__show run.txt"
result = regex_show_run(file_name)
hostname,domain,d_inf_ip = result

print(f"{'Hostname'.ljust(20)} : {hostname.rjust(22)}")
print(f"{'Domain name'.ljust(20)} : {domain.rjust(22)}")
print()
for inf,ip in d_inf_ip.items():
    print(f"Interface is {inf.ljust(22)} : {ip.rjust(30)}")
print()

# show ip route
print("Extract from ip route".title())
file_name = "2022-11-08__03__192.168.1.11__show ip route.txt"
result = regex_ip_route(file_name)
for subnet,out_inf in result.items():
    print(f"Subnet is {subnet.ljust(17)} : Outgoing Interfca is {out_inf.rjust(25)}")

