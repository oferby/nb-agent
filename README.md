## install SSH client
    pip install paramiko

## install gRPC
    pip install grpcio-tools

## gRPC Usage
    python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto