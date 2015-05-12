from tinyrpc.protocols.jsonrpc import JSONRPCProtocol

rpc = JSONRPCProtocol()

# again, code below is protocol-independent

# assuming you want to call method(*args, **kwargs)

request = rpc.create_request(method, args, kwargs)
reply = send_to_server_and_get_reply(request)

response = rpc.parse_reply(reply)

if hasattr(response, 'error'):
    pass
else:
    # the return value is found in response.result
    do_something_with(response.result)