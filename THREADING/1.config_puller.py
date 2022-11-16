from conf import CiscoConfigPull
import datetime,os,time
import concurrent.futures as cf

"""
Author : Rohit Verma
Feature : Use concurrent module to pull running configuration on multiple devices
"""

r1 = {"hostname":"192.168.1.11",
       "username":"admin",
       "password":"cisco" }
r2 = {"hostname":"192.168.1.12",
       "username":"admin",
       "password":"cisco" }
r3 = {"hostname":"192.168.1.13",
       "username":"admin",
       "password":"cisco" }
r4 = {"hostname":"192.168.1.14",
       "username":"admin",
       "password":"cisco" }
r5 = {"hostname":"192.168.1.15",
       "username":"admin",
       "password":"cisco" }
devices = [r1,r2,r3,r4,r5]

# Setting environment
os.chdir("/home/rohit/Documents/python/Udemy/para_miko/para_virtual/THREADING")

# Create a object and write into a file
class_start = time.perf_counter()
for device in devices:
       router = CiscoConfigPull(**device)
       hostname = router.session_connect()
       with cf.ThreadPoolExecutor() as executor:
              output = [executor.submit(router.config_pull_run)]
              for read_output in cf.as_completed(output):
                     file_name = f"{hostname}__show_run.txt"
                     with open(file_name,"w") as f:
                            f.write(read_output.result())
       router.session_close()
class_end = time.perf_counter()
print(f"Time took by class is {class_end-class_start}") 






                     

