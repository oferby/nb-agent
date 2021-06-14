import paramiko
import abc
import re

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

    @abc.abstractmethod
    def run_discovery(self):
        pass

    @abc.abstractmethod
    def get_agent_info(self):
        pass


class SSHAgent(Agent):

    def __init__(self, target, username, password):
        self.target = target
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.port = 22
        self.agent_dict = {self.target: {}}
        self.get_hostname()

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.target, self.port, self.username, self.password)

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
        return stdout.readline().strip()

    def get_agent_info(self):
        return self.agent_dict

    def read_lines(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.readlines()

    def read_line(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.readline().strip()

    def run_discovery(self):

        info_dict = {self.target: {"hostname": self.get_hostname()}}

        mainboad_info = {"0": {}}
        info_dict[self.target]["mainboard"] = mainboad_info

        lines = self.read_lines("lscpu | grep -E 'Arch|Vendor|CPU|NUMA'")

        for line in lines:
            splits = line.split(":")
            splits = [i.strip() for i in splits]

            if splits[0] == "Architecture":
                if "CPU" not in mainboad_info["0"]:
                    mainboad_info["0"]["CPU"] = {}
                mainboad_info["0"]["CPU"]["architecture"] = splits[1]
            elif splits[0] == "CPU(s)":
                mainboad_info["0"]["CPU"]["numberOfCPUs"] = splits[1]
            elif splits[0] == "Vendor ID":
                mainboad_info["0"]["CPU"]["vendor"] = splits[1]
            elif splits[0] == "CPU max MHz":
                mainboad_info["0"]["CPU"]["speed"] = splits[1]
            elif splits[0] == "Model name":
                mainboad_info["0"]["CPU"]["model"] = splits[1]

        info_dict[self.target]["mainboard"]["memory"] = self.read_line("free | awk '$0~/Mem/{print $2}'")

        lines = self.read_lines("ip addr")

        linecard = {"0": {}}
        interface = None
        for line in lines:
            line = line.strip()
            if line[0].isdigit():
                splits = re.split(": | ", line)
                interface = splits[1]
                linecard["0"][interface] = {}
                for i, s in enumerate(splits):
                    if s.startswith("<"):
                        if "LOWER_UP" in s:
                            linecard["0"][interface]["oper_status"] = "up"
                        elif "NO-CARRIER" in s:
                            linecard["0"][interface]["oper_status"] = "down"
                        if ",UP" in s:
                            linecard["0"][interface]["admin_status"] = "up"
                        else:
                            linecard["0"][interface]["admin_status"] = "down"
                    elif s == "mtu":
                        linecard["0"][interface]["mtu"] = splits[i + 1]
                    elif s == "qdisc":
                        linecard["0"][interface]["qdisc"] = splits[i + 1]
            elif line.startswith("link"):
                splits = line.split()
                linecard["0"][interface]["MAC"] = splits[1]
            elif line.startswith("inet "):
                splits = line.split()
                linecard["0"][interface]["IPv4"] = splits[1]
            elif line.startswith("inet6"):
                splits = line.split()
                linecard["0"][interface]["IPv6"] = splits[1]

        info_dict[self.target]["linecard"] = linecard

        self.agent_dict = info_dict

    def get_routing_table(self):

        if not self.is_alive():
            self.connect()

        stdin, stdout, stderr = self.client.exec_command('route')
        return stdout.readlines()
