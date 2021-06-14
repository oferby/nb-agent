import os
import sys
import socket
import agent.ssh_agent as ssh_agent
import json
import re

# print("hostname: ", socket.gethostname())

# target = 'localhost'
# agent = ssh_agent.SSHAgent(target, 'oferb', 'oferb')
#
target = '10.100.99.187'
agent = ssh_agent.SSHAgent(target, 'oferb', '123456')


client = agent.client

transport = agent.client.get_transport()
print("Transport: ", transport)

agent.connect()

print('After:')
transport = agent.client.get_transport()
print(transport)
if transport is not None:
    if not agent.client.get_transport().is_active():
        print("connection not active")
else:
    print("no transport.")

# print()
# print("\nRouting table:")
# [print(l) for l in agent.get_routing_table()]

info_dict = {target: {"hostname": agent.get_hostname()}}

mainboad_info = {"0": {}}
info_dict[target]["mainboard"] = mainboad_info


def read_lines(command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.readlines()


def read_line(command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.readline().strip()


lines = read_lines("lscpu | grep -E 'Arch|Vendor|CPU|NUMA'")

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

info_dict[target]["mainboard"]["memory"] = read_line("free | awk '$0~/Mem/{print $2}'")

lines = read_lines("ip addr")

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


info_dict[target]["linecard"] = linecard

print(json.dumps(info_dict))
