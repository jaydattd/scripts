cd test
python3 -m grpc_tools.protoc -I./resources/protos --python_out=. --grpc_python_out=. ./resources/protos/*
cp test.py test/*