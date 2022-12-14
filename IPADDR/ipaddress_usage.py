import ipaddress
from rich.console import Console
from rich.table import Table
from rich import print

table = Table(title="Subnet is 192.168.2.0")
table.add_column("IP address Module",justify="left")
table.add_column("Data",justify="left")
table.add_column("Commands",justify="left")
p = Console(record=True)
try:
    
    ip = ipaddress.ip_network("192.168.2.0/24")
    table.add_row("Broadcast",ip.broadcast_address.exploded,"ip.broadcast_address")
    table.add_row("Network Address",ip.network_address.exploded,"ip.network_address")
    table.add_row("Netmask",ip.netmask.exploded,"ip.netmask")
    table.add_row("Number of host IPs",str(ip.num_addresses),"ip.num_addresses")
    table.add_row("Subnet Mask",str(ip.prefixlen),"ip.prefixlen")
    table.add_row("Wild card of subnet",ip.hostmask.exploded,"ip.hostmask")
    table.add_row("Reverse Pointer for DNS",ip.reverse_pointer,"ip.reverse_pointer")
    table.add_row("Subnet with Maks",ip.with_prefixlen,"ip.with_prefixlen")
    table.add_row("IP Version",str(ip.version),"ip.version")
    p.print(table)

    # Validate if IP belongs to a subnet
    validated_ip = ipaddress.ip_network("192.168.2.5")
    print(ip.overlaps(validated_ip))

    #Another Way of validation
    ip_to_validated = ipaddress.ip_address("192.168.2.254")
    print(ip_to_validated in ip)

    # Use of exclude to generate a subnet
    to_to_be_excluded = ipaddress.ip_network("192.168.2.128/25")
    excluded_subnets = ip.address_exclude(to_to_be_excluded)
    for subnet in excluded_subnets:
        print(subnet)

except :
    p.print_exception()
    