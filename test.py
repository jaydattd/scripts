from concurrent import futures
import grpc

import Comp_a_pb2
import Comp_a_pb2_grpc

channel = grpc.insecure_channel('localhost:50055')
stub = Comp_a_pb2_grpc.CompAStub(channel)

componentAResponse = stub.getData(Comp_a_pb2.GetFullnameRequest(firstName="Jaydatt"))

print(componentAResponse)
