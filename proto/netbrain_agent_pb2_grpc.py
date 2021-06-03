# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import netbrain_agent_pb2 as netbrain__agent__pb2


class AgentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getHostInfo = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/getHostInfo',
                request_serializer=netbrain__agent__pb2.AgentHostInfoRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.AgentHostInfoResponse.FromString,
                )
        self.createAgent = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/createAgent',
                request_serializer=netbrain__agent__pb2.CreateAgentRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.CreateAgentResponse.FromString,
                )
        self.runDiscovery = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/runDiscovery',
                request_serializer=netbrain__agent__pb2.NodeDiscoveryRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.NodeDiscoveryResponse.FromString,
                )


class AgentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getHostInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def runDiscovery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getHostInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getHostInfo,
                    request_deserializer=netbrain__agent__pb2.AgentHostInfoRequest.FromString,
                    response_serializer=netbrain__agent__pb2.AgentHostInfoResponse.SerializeToString,
            ),
            'createAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.createAgent,
                    request_deserializer=netbrain__agent__pb2.CreateAgentRequest.FromString,
                    response_serializer=netbrain__agent__pb2.CreateAgentResponse.SerializeToString,
            ),
            'runDiscovery': grpc.unary_unary_rpc_method_handler(
                    servicer.runDiscovery,
                    request_deserializer=netbrain__agent__pb2.NodeDiscoveryRequest.FromString,
                    response_serializer=netbrain__agent__pb2.NodeDiscoveryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.toga.netbrain.service.AgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getHostInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/getHostInfo',
            netbrain__agent__pb2.AgentHostInfoRequest.SerializeToString,
            netbrain__agent__pb2.AgentHostInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/createAgent',
            netbrain__agent__pb2.CreateAgentRequest.SerializeToString,
            netbrain__agent__pb2.CreateAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def runDiscovery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/runDiscovery',
            netbrain__agent__pb2.NodeDiscoveryRequest.SerializeToString,
            netbrain__agent__pb2.NodeDiscoveryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)