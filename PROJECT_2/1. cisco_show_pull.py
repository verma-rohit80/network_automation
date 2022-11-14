from myconflib import Cisco_Config
import datetime,re

now = datetime.datetime.now().replace(microsecond=0)
now = str(now).split()
date_stamp = now[0]

with open("hostname.txt") as f:
    hostname_file = f.readlines()
    for file in hostname_file:
        hostname = file.strip()

# Invole show run
r1 = Cisco_Config(hostname,"admin","cisco")
r1.device_connect()
r1_show_run = r1.show_run()

# Write show run in a file
t = re.compile(r"(R1.*)",re.DOTALL)
show_run = t.search(r1_show_run).group()
file_name = f"{date_stamp} : show_run.txt"
with open(file_name,"w") as f_w:
    f_w.write(show_run)

# Invoke show version
show_ver = r1.show_version()
file_name = f"{date_stamp} : show_ver.txt"
with open(file_name,"w") as f_w:
    f_w.write(show_ver)

# Connection closed
r1.connect_close()