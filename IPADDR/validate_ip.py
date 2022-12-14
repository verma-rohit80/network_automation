import ipaddress
from rich.console import Console
console = Console(record = True)

subnet = ipaddress.ip_network("192.168.2.0/24")
lan = ipaddress.ip_address(input("Enter a subnet"))
if lan in subnet:
    print("True")
else:
    print("False")