# File name : config_puller.py
from conf import Config_puller
from dotenv import load_dotenv
import os,threading

load_dotenv()
with open("hostnames.txt") as f:
    f_host = f.readlines()

object_config = Config_puller()
for host in f_host:
    device = {
                "device_type" : "cisco_ios",
                "host" : host.strip(),
                "username" : os.getenv("username"),
                "password" : os.getenv("password")
    }

    temp_list_to_stop_threads = []
    output = threading.Thread(target=object_config.cisco_config_pull,kwargs=device)
    output.start()
    temp_list_to_stop_threads.append(output)
    for start in temp_list_to_stop_threads:
        start.join()


    