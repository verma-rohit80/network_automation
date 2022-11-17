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

for device in devices:
       with cf.ThreadPoolExecutor() as executor:
              out = [executor.submit(CiscoConfigPull,**device)]
              for return_output in cf.as_completed(out):
                     file_name = f"{return_output.result().hostname}__show_run.txt"
                     with open(file_name,"w") as f:
                            f.write(return_output.result().output)

               



                     

