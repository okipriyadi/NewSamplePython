from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
jsonprotocol = JSONRPCProtocol()
params = {        'Payload'     : "sjdkja",
                  'Ack'         : True,
                  'TailNum'     : 'PA-101'}
request = JSONRPCProtocol().create_request('check_alive')
print request.serialize()