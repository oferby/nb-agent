import os
import sys
import socket
import agent.ssh_agent as ssh_agent

print("hostname: ", socket.gethostname())

agent = ssh_agent.SSHAgent('localhost', 'oferb', 'oferb')

transport = agent.client.get_transport()
print("Transport: ", transport)

agent.connect()

print('After:')
transport = agent.client.get_transport()
print(transport)
if transport is not None:
    print(agent.client.get_transport().is_active())
else:
    print("no transport.")


print(agent.get_hostname())
print("\nRouting table:")
[print(l) for l in agent.get_routing_table()]


