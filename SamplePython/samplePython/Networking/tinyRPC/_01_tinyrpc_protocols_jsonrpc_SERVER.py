from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc import BadRequestError, RPCBatchRequest

rpc = JSONRPCProtocol()

# the code below is valid for all protocols, not just JSONRPC:

def handle_incoming_message(self, data):
    try:
        request = rpc.parse_request(data)
    except BadRequestError as e:
        # request was invalid, directly create response
        response = e.error_respond(e)
    else:
        # we got a valid request
        # the handle_request function is user-defined
        # and returns some form of response
        if hasattr(request, create_batch_response):
            response = request.create_batch_response(
                handle_request(req) for req in request
            )
        else:
            response = handle_request(request)

    # now send the response to the client
    if response != None:
         send_to_client(response.serialize())


def handle_request(request):
    try:
        # do magic with method, args, kwargs...
        return request.respond(result)
    except Exception as e:
        # for example, a method wasn't found
        return request.error_respond(e)