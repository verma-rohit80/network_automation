from paramiko import client,ssh_exception
import time,threading


class CiscoConfigPull:
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = 22

    def session_connect(self):
        try:
            self.session = client.SSHClient()
            self.session.set_missing_host_key_policy(client.AutoAddPolicy)
            self.session.connect(hostname=self.hostname,port=self.port,
                            username=self.username,password=self.password,
                            look_for_keys=False,allow_agent=False)
            print("Connection established")
            return self.hostname
        except ssh_exception.AuthenticationException:
            print("Password is wrong")
        except ssh_exception.NoValidConnectionsError:
            print("SSH Port is not Opened")

    def config_pull_run(self):
        self.object_access = self.session.invoke_shell()
        self.object_access.send("terminal length 0 \n")
        self.object_access.send("show run\n")
        time.sleep(3)
        output = self.object_access.recv(65535).decode()
        return output

    def session_close(self):
        self.object_access.close()
        print(f"{self.hostname} Connection is Closed")
