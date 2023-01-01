from CONF import Cisco
import threading,os,sys,rich

# Set path to look in CONF for hostnames
path = f"/home/rohit/Documents/python/Udemy/para_miko/para_virtual/PROJECT_3/venv/CONF"
os.chdir(path)
# os.chdir(path)

with open("hostnames.txt") as f:
    host = f.readlines()
os.chdir(os.getcwd())
choice = input("what output you seek (version|run|ospf|interfaces) ? ")
for hostname in host:
    device = {
            "device_type" : "cisco_ios",
            "host" : hostname.strip(),
            "username" : "admin",
            "password" : "cisco"
        }
    cisco = Cisco()
    excep = cisco.initialization(**device)
    if excep:
        print(excep)
    else:
        if choice == "version":
            temp = []
            config_thread = threading.Thread(target = cisco.sh_version)
            config_thread.start()
            temp.append(config_thread)
            for f in temp:
                f.join()
            cisco.connection_close()
        elif choice == "run":
            temp = []
            config_thread = threading.Thread(target = cisco.run)
            config_thread.start()
            temp.append(config_thread)
            for f in temp:
                f.join()
            cisco.connection_close()
        elif choice == "ospf":
            temp = []
            config_thread = threading.Thread(target = cisco.route_ospf)
            config_thread.start()
            temp.append(config_thread)
            for f in temp:
                f.join()
            cisco.connection_close()
        elif choice == "interfaces":
            temp = []
            config_thread = threading.Thread(target = cisco.interfaces)
            config_thread.start()
            temp.append(config_thread)
            for f in temp:
                f.join()
            cisco.connection_close()
        else:
            sys.exit()