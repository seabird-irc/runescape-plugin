# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import seabird_pb2 as seabird__pb2


class SeabirdStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpenSession = channel.unary_unary(
                '/seabird.Seabird/OpenSession',
                request_serializer=seabird__pb2.OpenSessionRequest.SerializeToString,
                response_deserializer=seabird__pb2.OpenSessionResponse.FromString,
                )
        self.Events = channel.unary_stream(
                '/seabird.Seabird/Events',
                request_serializer=seabird__pb2.EventsRequest.SerializeToString,
                response_deserializer=seabird__pb2.Event.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/seabird.Seabird/SendMessage',
                request_serializer=seabird__pb2.SendMessageRequest.SerializeToString,
                response_deserializer=seabird__pb2.SendMessageResponse.FromString,
                )
        self.SendRawMessage = channel.unary_unary(
                '/seabird.Seabird/SendRawMessage',
                request_serializer=seabird__pb2.SendRawMessageRequest.SerializeToString,
                response_deserializer=seabird__pb2.SendRawMessageResponse.FromString,
                )
        self.ListChannels = channel.unary_unary(
                '/seabird.Seabird/ListChannels',
                request_serializer=seabird__pb2.ListChannelsRequest.SerializeToString,
                response_deserializer=seabird__pb2.ListChannelsResponse.FromString,
                )
        self.GetChannelInfo = channel.unary_unary(
                '/seabird.Seabird/GetChannelInfo',
                request_serializer=seabird__pb2.ChannelInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.ChannelInfoResponse.FromString,
                )
        self.SetChannelInfo = channel.unary_unary(
                '/seabird.Seabird/SetChannelInfo',
                request_serializer=seabird__pb2.SetChannelInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.SetChannelInfoResponse.FromString,
                )
        self.JoinChannel = channel.unary_unary(
                '/seabird.Seabird/JoinChannel',
                request_serializer=seabird__pb2.JoinChannelRequest.SerializeToString,
                response_deserializer=seabird__pb2.JoinChannelResponse.FromString,
                )
        self.LeaveChannel = channel.unary_unary(
                '/seabird.Seabird/LeaveChannel',
                request_serializer=seabird__pb2.LeaveChannelRequest.SerializeToString,
                response_deserializer=seabird__pb2.LeaveChannelResponse.FromString,
                )
        self.ListPlugins = channel.unary_unary(
                '/seabird.Seabird/ListPlugins',
                request_serializer=seabird__pb2.ListPluginsRequest.SerializeToString,
                response_deserializer=seabird__pb2.ListPluginsResponse.FromString,
                )
        self.GetPluginInfo = channel.unary_unary(
                '/seabird.Seabird/GetPluginInfo',
                request_serializer=seabird__pb2.PluginInfoRequest.SerializeToString,
                response_deserializer=seabird__pb2.PluginInfoResponse.FromString,
                )


class SeabirdServicer(object):
    """Missing associated documentation comment in .proto file"""

    def OpenSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Events(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRawMessage(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChannels(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetChannelInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinChannel(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveChannel(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlugins(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPluginInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SeabirdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OpenSession': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenSession,
                    request_deserializer=seabird__pb2.OpenSessionRequest.FromString,
                    response_serializer=seabird__pb2.OpenSessionResponse.SerializeToString,
            ),
            'Events': grpc.unary_stream_rpc_method_handler(
                    servicer.Events,
                    request_deserializer=seabird__pb2.EventsRequest.FromString,
                    response_serializer=seabird__pb2.Event.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=seabird__pb2.SendMessageRequest.FromString,
                    response_serializer=seabird__pb2.SendMessageResponse.SerializeToString,
            ),
            'SendRawMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRawMessage,
                    request_deserializer=seabird__pb2.SendRawMessageRequest.FromString,
                    response_serializer=seabird__pb2.SendRawMessageResponse.SerializeToString,
            ),
            'ListChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListChannels,
                    request_deserializer=seabird__pb2.ListChannelsRequest.FromString,
                    response_serializer=seabird__pb2.ListChannelsResponse.SerializeToString,
            ),
            'GetChannelInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelInfo,
                    request_deserializer=seabird__pb2.ChannelInfoRequest.FromString,
                    response_serializer=seabird__pb2.ChannelInfoResponse.SerializeToString,
            ),
            'SetChannelInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SetChannelInfo,
                    request_deserializer=seabird__pb2.SetChannelInfoRequest.FromString,
                    response_serializer=seabird__pb2.SetChannelInfoResponse.SerializeToString,
            ),
            'JoinChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinChannel,
                    request_deserializer=seabird__pb2.JoinChannelRequest.FromString,
                    response_serializer=seabird__pb2.JoinChannelResponse.SerializeToString,
            ),
            'LeaveChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveChannel,
                    request_deserializer=seabird__pb2.LeaveChannelRequest.FromString,
                    response_serializer=seabird__pb2.LeaveChannelResponse.SerializeToString,
            ),
            'ListPlugins': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlugins,
                    request_deserializer=seabird__pb2.ListPluginsRequest.FromString,
                    response_serializer=seabird__pb2.ListPluginsResponse.SerializeToString,
            ),
            'GetPluginInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPluginInfo,
                    request_deserializer=seabird__pb2.PluginInfoRequest.FromString,
                    response_serializer=seabird__pb2.PluginInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'seabird.Seabird', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Seabird(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def OpenSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/OpenSession',
            seabird__pb2.OpenSessionRequest.SerializeToString,
            seabird__pb2.OpenSessionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Events(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/seabird.Seabird/Events',
            seabird__pb2.EventsRequest.SerializeToString,
            seabird__pb2.Event.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/SendMessage',
            seabird__pb2.SendMessageRequest.SerializeToString,
            seabird__pb2.SendMessageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRawMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/SendRawMessage',
            seabird__pb2.SendRawMessageRequest.SerializeToString,
            seabird__pb2.SendRawMessageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/ListChannels',
            seabird__pb2.ListChannelsRequest.SerializeToString,
            seabird__pb2.ListChannelsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/GetChannelInfo',
            seabird__pb2.ChannelInfoRequest.SerializeToString,
            seabird__pb2.ChannelInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetChannelInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/SetChannelInfo',
            seabird__pb2.SetChannelInfoRequest.SerializeToString,
            seabird__pb2.SetChannelInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/JoinChannel',
            seabird__pb2.JoinChannelRequest.SerializeToString,
            seabird__pb2.JoinChannelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LeaveChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/LeaveChannel',
            seabird__pb2.LeaveChannelRequest.SerializeToString,
            seabird__pb2.LeaveChannelResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPlugins(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/ListPlugins',
            seabird__pb2.ListPluginsRequest.SerializeToString,
            seabird__pb2.ListPluginsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPluginInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/seabird.Seabird/GetPluginInfo',
            seabird__pb2.PluginInfoRequest.SerializeToString,
            seabird__pb2.PluginInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)