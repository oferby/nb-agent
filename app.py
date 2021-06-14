import sys
import socket
import grpc
from concurrent import futures
import json

sys.path.insert(0, './proto')
sys.path.insert(1, './agent')

from proto import netbrain_agent_pb2 as agent_pb2
from proto import netbrain_agent_pb2_grpc as agent_grpc
from agent import ssh_agent


def append_to_net_element(uri, net_elements):
    NetElement = agent_pb2.NetElement(
        URI=uri
    )

    net_elements.append(NetElement)
    return net_elements


class AgentServicer(agent_grpc.AgentServiceServicer):

    def __init__(self):
        self.agents = {}
        self.hostId = None
        self.hostname = socket.gethostname()
        self.executor = futures.ThreadPoolExecutor(max_workers=10)

        self.command_dict = {
            'shutDownHostAgent': self.shut_down
        }

        self.agents_info_dict = {}

    def getHostInfo(self, request, context):
        print("got request host info.")
        self.hostId = request.hostId

        return agent_pb2.AgentHostInfoResponse(hostId=self.hostId, hostName=self.hostname,
                                               numOfAgents=len(self.agents.keys()))

    def sendCommand(self, request, context):
        return self.command_dict[request.command]()

    def createAgent(self, request, context):
        target = request.target
        print("creating agent for: " + target)

        if target in self.agents:
            return agent_pb2.CreateAgentResponse(ack=True)

        agent = ssh_agent.SSHAgent(target, request.username, request.password)
        self.agents[target] = agent
        self.executor.submit(self.run_agent_discovery, agent)
        return agent_pb2.CreateAgentResponse(ack=True)

    @staticmethod
    def run_agent_discovery(agent):
        print("running agent discovery task")
        agent.run_discovery()

    def getAgentInformation(self, request, context):
        target = request.target
        print("request agent info for target: " + target)
        agent = self.agents[target]
        net_elements = []
        json_str = json.dumps(agent.get_agent_info())
        append_to_net_element(json_str, net_elements)

        return agent_pb2.NodeDiscoveryResponse(target=target, netElements=net_elements)

    def deleteAgent(self, request, context):
        target = request.target
        print("deleting agent " + target)
        if target in self.agents:
            agent = self.agents[target]
            agent.disconnect()
            del self.agents[target]
            del agent
            return agent_pb2.DeleteAgentResponse(ack=True)
        else:
            print("agent not found.")
            return agent_pb2.DeleteAgentResponse(ack=False)

    def shut_down(self):
        print("clearing all agents.....")
        self.agents.clear()
        return agent_pb2.HostAgentCommandResponse(errorCode=0)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_grpc.add_AgentServiceServicer_to_server(
        AgentServicer(), server)

    server.add_insecure_port('[::]:51051')
    server.start()
    print("Server Started!")
    server.wait_for_termination()


serve()
