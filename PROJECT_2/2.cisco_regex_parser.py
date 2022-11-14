from myconflib import Regex_parser
import os

# Parding show versionb
os.chdir(r"/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_2/")
file_name = "2022-11-14 : show_ver.txt"
with open(file_name) as f:
    filename = f.read()

r1 = Regex_parser()
uptime,board = r1.show_version_parser(filename)

# Parding show run
os.chdir(r"/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_2/")
file_name = "2022-11-14 : show_run.txt"
with open(file_name) as f:
    filename = f.read()

r1 = Regex_parser()
hostname,domain = r1.show_run_parser(filename)
# print(hostname,domain)

# Parse interfaces with IP from show run
os.chdir(r"/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_2/")
file_name = "2022-11-14 : show_run.txt"
with open(file_name) as f:
    filename = f.read()

r1 = Regex_parser()
interfaces = r1.show_run_interface_parser(filename)

# Wring putput from show versiona nd run into file
with open("parsed_text","w") as f:
    f.write("Interfaces with ip details\n".title())
    for interface,ip in interfaces:
        f.write(f"{interface.ljust(35)}: {ip.rjust(34)}\n")
    f.write("\n")
    f.write("Uptime and Board ID\n".title())
    f.write(f"Uptime is {uptime} and Board ID is {board}\n")
    f.write("\n")
    f.write("Hostname and domainname \n".title())
    f.write(f"Hostname is {hostname} and  DOmain name  is {domain}\n")