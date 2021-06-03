import sys
import socket
import grpc
from concurrent import futures

sys.path.insert(0, './proto')
sys.path.insert(1, './agent')

from proto import netbrain_agent_pb2 as agent_pb2
from proto import netbrain_agent_pb2_grpc as agent_grpc
from agent import ssh_agent


class AgentServicer(agent_grpc.AgentServiceServicer):

    def __init__(self):
        self.agents = {}
        self.hostId = None
        self.hostname = socket.gethostname()

    def getHostInfo(self, request, context):
        self.hostId = request.hostId

        return agent_pb2.AgentHostInfoResponse(hostId=self.hostId, hostName=self.hostname,
                                               numOfAgents=len(self.agents.keys()))

    def createAgent(self, request, context):
        print("creating agent for: " + request.host)
        host = request.host

        if host in self.agents:
            return agent_pb2.CreateAgentResponse(ack=False)

        agent = ssh_agent.SSHAgent(host, request.username, request.password)
        self.agents[request.host] = agent

        return agent_pb2.CreateAgentResponse(ack=True)

    def runDiscovery(self, request, context):
        print("request discovery for host: " + request.host)
        host = request.host
        agent = self.agents[host]
        hostname = agent.get_hostname()

        netElements = []

        NetElement = agent_pb2.NetElement(
            URI='\\host\\' + host
        )

        netElements.append(NetElement)

        NetElement = agent_pb2.NetElement(
            URI='\\host\\' + host + '\\name\\' + hostname
        )

        netElements.append(NetElement)

        return agent_pb2.NodeDiscoveryResponse(host=host, netElements=netElements)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_grpc.add_AgentServiceServicer_to_server(
        AgentServicer(), server)

    server.add_insecure_port('[::]:51051')
    server.start()
    print("Server Started!")
    server.wait_for_termination()


serve()
