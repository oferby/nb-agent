## install SSH client
    pip install paramiko

## install gRPC
    pip install grpcio-tools

## gRPC Usage
    python -m grpc_tools.protoc -I proto --python_out=proto --grpc_python_out=proto proto/netbrain_agent.proto


## URI
\host\{id}
\host\{id}\name\{name}
