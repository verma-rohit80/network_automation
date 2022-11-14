from paramiko import client,ssh_exception
import time


class Cisco_Config:
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def device_connect(self):
        try:
            session = client.SSHClient()
            session.set_missing_host_key_policy(client.AutoAddPolicy)
            session.connect(hostname=self.hostname,port = 22,
                            username=self.username,password=self.password,
                            look_for_keys=False,allow_agent=False)

            self.device_connect = session.invoke_shell() 
            self.device_connect.send("terminal length 0\n")
            time.sleep(2)
            print("Connection estblished")      
        except ssh_exception.AuthenticationException:
            print("Password Error")
        except ssh_exception.NoValidConnectionsError:
            print("Check Hostname") 

    def show_run(self):
        self.device_connect.send("show run \n")
        time.sleep(7)
        output = self.device_connect.recv(65535).decode()
        return output
    def show_version(self):
        self.device_connect.send("show version \n")
        time.sleep(7)
        output = self.device_connect.recv(65535).decode()
        return output

    def connect_close(self):
        self.device_connect.close()
        print("Connection Closed \n")