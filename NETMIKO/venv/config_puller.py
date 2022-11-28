from master import Cisco
from dotenv import load_dotenv
import os
import  concurrent.futures as cf
import threading

load_dotenv()
with open("hostname.txt") as f:
    hostnames = f.readlines()

for hostname in hostnames:
    count = 1
    device = {
              "device_type" : "cisco_ios",
              "host" : hostname.strip(),
              "username" : os.getenv("username"),
              "password" : os.getenv("password")
    }
    
    

#  With concurrent
#     with cf.ThreadPoolExecutor() as executor:
#         out = executor.submit(Cisco,**device)
#     # out.result()
    
#  With Threading
    temp = []
    config_thread = threading.Thread(target=Cisco,kwargs=device)
    config_thread.start()
    temp.append(config_thread)
    for f in temp:
        f.join()
