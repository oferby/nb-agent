import paramiko


class SSHAgent:
    def __init__(self, ipAddress, username, password):
        self.ip = ipAddress
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.port = 22

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, self.port, self.username, self.password)

    def get_hostname(self):
        stdin, stdout, stderr = self.client.exec_command('hostname')
        return stdout.readline()

    def get_routing_table(self):
        stdin, stdout, stderr = self.client.exec_command('route')
        return stdout.readlines()


