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
        self.sendCommand = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/sendCommand',
                request_serializer=netbrain__agent__pb2.HostAgentCommandRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.HostAgentCommandResponse.FromString,
                )
        self.createAgent = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/createAgent',
                request_serializer=netbrain__agent__pb2.CreateAgentRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.CreateAgentResponse.FromString,
                )
        self.getAgentInformation = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/getAgentInformation',
                request_serializer=netbrain__agent__pb2.NodeDiscoveryRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.NodeDiscoveryResponse.FromString,
                )
        self.deleteAgent = channel.unary_unary(
                '/com.toga.netbrain.service.AgentService/deleteAgent',
                request_serializer=netbrain__agent__pb2.DeleteAgentRequest.SerializeToString,
                response_deserializer=netbrain__agent__pb2.DeleteAgentResponse.FromString,
                )


class AgentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getHostInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAgentInformation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteAgent(self, request, context):
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
            'sendCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.sendCommand,
                    request_deserializer=netbrain__agent__pb2.HostAgentCommandRequest.FromString,
                    response_serializer=netbrain__agent__pb2.HostAgentCommandResponse.SerializeToString,
            ),
            'createAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.createAgent,
                    request_deserializer=netbrain__agent__pb2.CreateAgentRequest.FromString,
                    response_serializer=netbrain__agent__pb2.CreateAgentResponse.SerializeToString,
            ),
            'getAgentInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.getAgentInformation,
                    request_deserializer=netbrain__agent__pb2.NodeDiscoveryRequest.FromString,
                    response_serializer=netbrain__agent__pb2.NodeDiscoveryResponse.SerializeToString,
            ),
            'deleteAgent': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteAgent,
                    request_deserializer=netbrain__agent__pb2.DeleteAgentRequest.FromString,
                    response_serializer=netbrain__agent__pb2.DeleteAgentResponse.SerializeToString,
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
    def sendCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/sendCommand',
            netbrain__agent__pb2.HostAgentCommandRequest.SerializeToString,
            netbrain__agent__pb2.HostAgentCommandResponse.FromString,
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
    def getAgentInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/getAgentInformation',
            netbrain__agent__pb2.NodeDiscoveryRequest.SerializeToString,
            netbrain__agent__pb2.NodeDiscoveryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteAgent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.toga.netbrain.service.AgentService/deleteAgent',
            netbrain__agent__pb2.DeleteAgentRequest.SerializeToString,
            netbrain__agent__pb2.DeleteAgentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
