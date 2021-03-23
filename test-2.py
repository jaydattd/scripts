from concurrent import futures
import grpc

import Comp_a_pb2
import Comp_a_pb2_grpc
import Comp_b_pb2
import Comp_b_pb2_grpc
import Comp_c_pb2
import Comp_c_pb2_grpc

channel = grpc.insecure_channel('localhost:4770')

stub = Comp_a_pb2_grpc.CompAStub(channel)
componentAResponse = stub.getData(Comp_a_pb2.GetFullnameRequest(firstName="Jaydatt"))

print(componentAResponse)


# Mock data code

stub = Comp_b_pb2_grpc.CompBStub(channel)
lastnameResponse = stub.getData(Comp_b_pb2.GetLastnameRequest(firstName="Jaydatt"))

print(lastnameResponse)


stub = Comp_c_pb2_grpc.CompCStub(channel)
companyNameResponse = stub.getCompany(Comp_c_pb2.GetCompany(firstName="Jaydatt"))

print(companyNameResponse)
