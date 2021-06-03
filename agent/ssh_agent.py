import paramiko
import abc


class Agent:
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def is_alive(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def get_hostname(self):
        pass


class SSHAgent(Agent):

    def __init__(self, ip_address, username, password):
        self.ip = ip_address
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.port = 22

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, self.port, self.username, self.password)

    def is_alive(self):
        if self.client.get_transport() is not None and self.client.get_transport().is_active():
            return True
        return False

    def disconnect(self):

        if not self.is_alive():
            return

        self.client.close()

    def get_hostname(self):

        if not self.is_alive():
            self.connect()

        stdin, stdout, stderr = self.client.exec_command('hostname')
        return stdout.readline()

    def get_routing_table(self):

        if not self.is_alive():
            self.connect()

        stdin, stdout, stderr = self.client.exec_command('route')
        return stdout.readlines()
