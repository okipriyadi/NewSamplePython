from twisted.application import service
from ubuntu_sso.utils.ipc import LOCALHOST

application = service.Application("SMTP Client Tutorial")

"""
twisted.application.internet is another application service module. It provides services 
for establishing outgoing connections (as well as creating network servers, 
though we are not interested in those parts for the moment). 

twisted.internet.protocol : provides base implementations of many of the core Twisted 
concepts, such as factories and protocols .
"""
from twisted.application import internet
from twisted.internet import protocol

smtpClientFactory = protocol.ClientFactory()
#Untuk sementara pakai loclhost dan port 25 yang biasa digunakan untuk mail
smtpClientService = internet.TCPClient('localhost', 25, smtpClientFactory)
smtpClientService.setServiceParent(application)
"""
Client factories are responsible for constructing protocol instances whenever 
connections are established. They may be required to create just one instance, 
or many instances if many different connections are established, or they may never be 
required to create one at all, if no connection ever manages to be established.

Now that we have a client factory, we'll need to hook it up to the network somehow. 
The next line does just that:

smtpClientService = internet.TCPClient(None, None, smtpClientFactory)
We'll ignore the first two arguments to internet.TCPClient for the moment and instead 
focus on the third. TCPClient is one of those application service classes. 
It creates TCP connections to a specified address and then uses its third argument, 
a client factory , to get a protocol instance . It then associates the TCP connection 
with the protocol instance and gets out of the way.

We can try to run smtpclient-2.tac the same way we ran smtpclient-1.tac , 
but the results might be a little disappointing:

What happened? Those first two arguments to TCPClient turned out to be important after all. We'll get to them in the next example.
"""