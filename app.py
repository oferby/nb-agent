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
        pass

    def runDiscovery(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_grpc.add_AgentServiceServicer_to_server(
        AgentServicer(), server)

    server.add_insecure_port('[::]:51051')
    server.start()
    print("Server Started!")
    server.wait_for_termination()


serve()
