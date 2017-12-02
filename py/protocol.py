# -*- coding: utf-8 -*-

from autobahn.twisted.websocket import WebSocketServerProtocol


class Protocol(WebSocketServerProtocol):
    def __init__(self):
        WebSocketServerProtocol.__init__(self)

        self.ip = None

    def onOpen(self):
        print('WebSocket connection open.')

        self.factory.register(self)

    def onClose(self, wasClean, code, reason):
        print('WebSocket connection closed: {}'.format(reason))

    def connectionLost(self, reason):
        print('WebSocket connection lost: {}'.format(reason))

        self.factory.unregister(self)

    def onConnect(self, request):
        print('Client connecting: {}'.format(request.peer))

        self.ip = request.peer.split(':')[1]

    def onMessage(self, payload, isBinary):
        if isBinary:
            print('Binary message received: {0} bytes'.format(len(payload)))
        else:
            msg = payload.decode('utf8')

            if msg == 'todas_vagas':
                self.factory.todas_vagas(self)
                
            elif '<&>' in msg:
                code, client_msg = msg.split('<&>')

                if code == 'add_vaga':
                    self.factory.add_vaga(self,lat,lon)
                
                elif code == 'vaga_positiva':
                    self.factory.vaga_positiva(self,lat,lon)

                elif code == 'vaga_negativa':
                    self.factory.vaga_negativa(self,lat,lon)
                    
