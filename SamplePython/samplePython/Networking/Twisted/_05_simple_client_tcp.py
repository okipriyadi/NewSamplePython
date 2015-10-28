from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor


class PoetryProtocol(Protocol):

    poem = ''

    def dataReceived(self, data):
        self.poem += data

    def connectionLost(self, reason):
        pass


class PoetryClientFactory(ClientFactory):

    protocol = PoetryProtocol

    def __init__(self):
        pass

def poetry_main():
    factory = PoetryClientFactory()
    reactor.connectTCP('localhost', 5555, factory)
    reactor.run()

    for poem in poems:
        print poem


if __name__ == '__main__':
    poetry_main()