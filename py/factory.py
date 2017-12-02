# -*- coding: utf-8 -*-


from autobahn.twisted.websocket import WebSocketServerFactory

from database import Database


class Factory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)

        self.ip_admin = None
        self.clients = []

        self.db = Database()
    
    def todas_vagas(self,client):

        d = self.db.todas_vagas()

        def callback(args):
            lista = []

            for value in args:
                print(value)
                lista.append(value)
            
            msg = "todas_vagas<&>" + ';'.join(lista)

            client.sendMessage(msg.encode(encoding='utf_8'))

        d.addCallback(callback)

    def add_vaga(self,client, lat, lon):

        d = self.db.add_vaga()

        def callback(args):

            msg = "feedback<&>" + 'Vaga adicionada'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)

    def vaga_positiva(self,client, lat, lon):

        d = self.db.vaga_positiva()

        def callback(args):

            msg = "feedback<&>" + 'Vaga joinha'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)

    def vaga_negativa(self,client, lat, lon):

        d = self.db.vaga_negativa()

        def callback(args):

            msg = "feedback<&>" + 'Vaga NÃO joinha'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)
