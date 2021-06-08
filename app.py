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

        self.command_dict = {
            'shutDownHostAgent': self.shut_down
        }

    def getHostInfo(self, request, context):
        print("got request host info.")
        self.hostId = request.hostId

        return agent_pb2.AgentHostInfoResponse(hostId=self.hostId, hostName=self.hostname,
                                               numOfAgents=len(self.agents.keys()))

    def sendCommand(self, request, context):
        return self.command_dict[request.command]()

    def createAgent(self, request, context):
        agent_name = request.agent
        print("creating agent for: " + agent_name)

        if agent_name in self.agents:
            return agent_pb2.CreateAgentResponse(ack=False)

        agent = ssh_agent.SSHAgent(agent_name, request.username, request.password)
        self.agents[agent_name] = agent

        return agent_pb2.CreateAgentResponse(ack=True)

    def runDiscovery(self, request, context):
        agent_name = request.agent
        print("request discovery for host: " + agent_name)
        agent = self.agents[agent_name]
        hostname = agent.get_hostname()

        net_elements = []

        host_uri = '\\hostAgent\\' + self.hostId
        self.get_net_element(host_uri, net_elements)

        agent_uri = host_uri + '\\agent\\' + agent_name
        self.get_net_element(agent_uri, net_elements)

        uri = agent_uri + '\\name\\' + hostname
        self.get_net_element(uri, net_elements)

        return agent_pb2.NodeDiscoveryResponse(agent=agent_name, netElements=net_elements)

    def shut_down(self):
        print("clearing all agents.....")
        self.agents.clear()
        return agent_pb2.HostAgentResponse(errorCode=0)

    def get_net_element(self, uri, net_elements):
        NetElement = agent_pb2.NetElement(
            URI=uri
        )

        net_elements.append(NetElement)
        return net_elements


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_grpc.add_AgentServiceServicer_to_server(
        AgentServicer(), server)

    server.add_insecure_port('[::]:51051')
    server.start()
    print("Server Started!")
    server.wait_for_termination()


serve()
