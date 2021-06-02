import os
import sys
import socket
import agent.ssh_agent as ssh_agent

print("hostname: ", socket.gethostname())

agent = ssh_agent.SSHAgent('localhost', 'oferb', 'oferb')

agent.connect()

print(agent.get_hostname())
[print(l) for l in agent.get_routing_table()]


