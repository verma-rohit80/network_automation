import os
import textfsm

with open("CISCO_OUTPUTS/192.168.1.11__show_interface_brief.txt") as f:
    f_int = f.read()


home_dir = os.path.expanduser("~")
# template_dir = os.path.join(
#     home_dir,"Documents","python","Udemy","para_miko","para_virtual","NETMIKO","venv",
#     "lib","python3.10","site-packages","ntc_templates","templates/"
# )
template_dir = os.path.join(
    "lib","python3.10","site-packages","ntc_templates","templates/"

)
print(f"{template_dir}cisco_ios_show_ip_interface_brief.textfsm")

template = open(f"{template_dir}cisco_ios_show_ip_interface_brief.textfsm")
re_table = textfsm.TextFSM(template)
res = re_table.ParseText(f_int)
print(res)


# /home/rohit/Documents/python/Udemy/para_miko/para_virtual/NETMIKO/venv/lib/python3.10/site-packages/ntc_templates/templates/
# /lib/python3.10/site-packages/ntc_templates/templates