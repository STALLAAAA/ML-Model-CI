# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import service_pb2 as proto_dot_service__pb2


class PredictStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Infer = channel.unary_unary(
        '/Predict/Infer',
        request_serializer=proto_dot_service__pb2.InferRequest.SerializeToString,
        response_deserializer=proto_dot_service__pb2.InferResponse.FromString,
        )
    self.StreamInfer = channel.stream_stream(
        '/Predict/StreamInfer',
        request_serializer=proto_dot_service__pb2.InferRequest.SerializeToString,
        response_deserializer=proto_dot_service__pb2.InferResponse.FromString,
        )


class PredictServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Infer(self, request, context):
    """Inference
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamInfer(self, request_iterator, context):
    """Stream Interface
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Infer': grpc.unary_unary_rpc_method_handler(
          servicer.Infer,
          request_deserializer=proto_dot_service__pb2.InferRequest.FromString,
          response_serializer=proto_dot_service__pb2.InferResponse.SerializeToString,
      ),
      'StreamInfer': grpc.stream_stream_rpc_method_handler(
          servicer.StreamInfer,
          request_deserializer=proto_dot_service__pb2.InferRequest.FromString,
          response_serializer=proto_dot_service__pb2.InferResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Predict', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))