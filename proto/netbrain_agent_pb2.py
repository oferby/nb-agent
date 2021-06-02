# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: netbrain_agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='netbrain_agent.proto',
  package='com.toga.netbrain.service',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14netbrain_agent.proto\x12\x19\x63om.toga.netbrain.service\"d\n\x12\x43reateAgentRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\"\"\n\x13\x43reateAgentResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"&\n\x14\x41gentHostInfoRequest\x12\x0e\n\x06hostId\x18\x01 \x01(\t\"N\n\x15\x41gentHostInfoResponse\x12\x0e\n\x06hostId\x18\x01 \x01(\t\x12\x10\n\x08hostName\x18\x02 \x01(\t\x12\x13\n\x0bnumOfAgents\x18\x03 \x01(\x05\"\'\n\x14NodeDiscoveryRequest\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\"c\n\x15NodeDiscoveryResponse\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\x12\x39\n\nnetElement\x18\x02 \x03(\x0b\x32%.com.toga.netbrain.service.NetElement\"(\n\nNetElement\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t2\xef\x01\n\x0c\x41gentService\x12l\n\x0b\x63reateAgent\x12-.com.toga.netbrain.service.CreateAgentRequest\x1a..com.toga.netbrain.service.CreateAgentResponse\x12q\n\x0crunDiscovery\x12/.com.toga.netbrain.service.NodeDiscoveryRequest\x1a\x30.com.toga.netbrain.service.NodeDiscoveryResponseB\x02P\x01\x62\x06proto3'
)




_CREATEAGENTREQUEST = _descriptor.Descriptor(
  name='CreateAgentRequest',
  full_name='com.toga.netbrain.service.CreateAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='com.toga.netbrain.service.CreateAgentRequest.nodeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='com.toga.netbrain.service.CreateAgentRequest.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='com.toga.netbrain.service.CreateAgentRequest.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='com.toga.netbrain.service.CreateAgentRequest.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.toga.netbrain.service.CreateAgentRequest.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=151,
)


_CREATEAGENTRESPONSE = _descriptor.Descriptor(
  name='CreateAgentResponse',
  full_name='com.toga.netbrain.service.CreateAgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.toga.netbrain.service.CreateAgentResponse.ack', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=187,
)


_AGENTHOSTINFOREQUEST = _descriptor.Descriptor(
  name='AgentHostInfoRequest',
  full_name='com.toga.netbrain.service.AgentHostInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='com.toga.netbrain.service.AgentHostInfoRequest.hostId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=227,
)


_AGENTHOSTINFORESPONSE = _descriptor.Descriptor(
  name='AgentHostInfoResponse',
  full_name='com.toga.netbrain.service.AgentHostInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='com.toga.netbrain.service.AgentHostInfoResponse.hostId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostName', full_name='com.toga.netbrain.service.AgentHostInfoResponse.hostName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numOfAgents', full_name='com.toga.netbrain.service.AgentHostInfoResponse.numOfAgents', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=307,
)


_NODEDISCOVERYREQUEST = _descriptor.Descriptor(
  name='NodeDiscoveryRequest',
  full_name='com.toga.netbrain.service.NodeDiscoveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='com.toga.netbrain.service.NodeDiscoveryRequest.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=348,
)


_NODEDISCOVERYRESPONSE = _descriptor.Descriptor(
  name='NodeDiscoveryResponse',
  full_name='com.toga.netbrain.service.NodeDiscoveryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='com.toga.netbrain.service.NodeDiscoveryResponse.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='netElement', full_name='com.toga.netbrain.service.NodeDiscoveryResponse.netElement', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=449,
)


_NETELEMENT = _descriptor.Descriptor(
  name='NetElement',
  full_name='com.toga.netbrain.service.NetElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='com.toga.netbrain.service.NetElement.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.toga.netbrain.service.NetElement.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=491,
)

_NODEDISCOVERYRESPONSE.fields_by_name['netElement'].message_type = _NETELEMENT
DESCRIPTOR.message_types_by_name['CreateAgentRequest'] = _CREATEAGENTREQUEST
DESCRIPTOR.message_types_by_name['CreateAgentResponse'] = _CREATEAGENTRESPONSE
DESCRIPTOR.message_types_by_name['AgentHostInfoRequest'] = _AGENTHOSTINFOREQUEST
DESCRIPTOR.message_types_by_name['AgentHostInfoResponse'] = _AGENTHOSTINFORESPONSE
DESCRIPTOR.message_types_by_name['NodeDiscoveryRequest'] = _NODEDISCOVERYREQUEST
DESCRIPTOR.message_types_by_name['NodeDiscoveryResponse'] = _NODEDISCOVERYRESPONSE
DESCRIPTOR.message_types_by_name['NetElement'] = _NETELEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAgentRequest = _reflection.GeneratedProtocolMessageType('CreateAgentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAGENTREQUEST,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.CreateAgentRequest)
  })
_sym_db.RegisterMessage(CreateAgentRequest)

CreateAgentResponse = _reflection.GeneratedProtocolMessageType('CreateAgentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAGENTRESPONSE,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.CreateAgentResponse)
  })
_sym_db.RegisterMessage(CreateAgentResponse)

AgentHostInfoRequest = _reflection.GeneratedProtocolMessageType('AgentHostInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTHOSTINFOREQUEST,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.AgentHostInfoRequest)
  })
_sym_db.RegisterMessage(AgentHostInfoRequest)

AgentHostInfoResponse = _reflection.GeneratedProtocolMessageType('AgentHostInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTHOSTINFORESPONSE,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.AgentHostInfoResponse)
  })
_sym_db.RegisterMessage(AgentHostInfoResponse)

NodeDiscoveryRequest = _reflection.GeneratedProtocolMessageType('NodeDiscoveryRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEDISCOVERYREQUEST,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.NodeDiscoveryRequest)
  })
_sym_db.RegisterMessage(NodeDiscoveryRequest)

NodeDiscoveryResponse = _reflection.GeneratedProtocolMessageType('NodeDiscoveryResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEDISCOVERYRESPONSE,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.NodeDiscoveryResponse)
  })
_sym_db.RegisterMessage(NodeDiscoveryResponse)

NetElement = _reflection.GeneratedProtocolMessageType('NetElement', (_message.Message,), {
  'DESCRIPTOR' : _NETELEMENT,
  '__module__' : 'netbrain_agent_pb2'
  # @@protoc_insertion_point(class_scope:com.toga.netbrain.service.NetElement)
  })
_sym_db.RegisterMessage(NetElement)


DESCRIPTOR._options = None

_AGENTSERVICE = _descriptor.ServiceDescriptor(
  name='AgentService',
  full_name='com.toga.netbrain.service.AgentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=494,
  serialized_end=733,
  methods=[
  _descriptor.MethodDescriptor(
    name='createAgent',
    full_name='com.toga.netbrain.service.AgentService.createAgent',
    index=0,
    containing_service=None,
    input_type=_CREATEAGENTREQUEST,
    output_type=_CREATEAGENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='runDiscovery',
    full_name='com.toga.netbrain.service.AgentService.runDiscovery',
    index=1,
    containing_service=None,
    input_type=_NODEDISCOVERYREQUEST,
    output_type=_NODEDISCOVERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENTSERVICE)

DESCRIPTOR.services_by_name['AgentService'] = _AGENTSERVICE

# @@protoc_insertion_point(module_scope)