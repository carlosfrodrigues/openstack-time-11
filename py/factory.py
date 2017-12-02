# -*- coding: utf-8 -*-


from autobahn.twisted.websocket import WebSocketServerFactory

from database import Database


class Factory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)

        self.ip_admin = None
        self.clients = []

        self.db = Database()

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))

            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))

            self.clients.remove(client)


    def todas_vagas(self,client):

        d = self.db.todas_vagas()

        def callback(args):

            lista = [str(x) for arg in args for x in arg]
            
            msg = "todas_vagas<&>" + ';'.join(lista)

            client.sendMessage(msg.encode(encoding='utf_8'))

        d.addCallback(callback)

    def add_vaga(self,client, lat, lon):

        d = self.db.add_vaga(lat,lon)

        def callback(args):

            msg = "feedback<&>" + 'Vaga adicionada'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)

    def positivar_vaga(self,client, lat, lon):

        d = self.db.consulta_positiva(lat,lon)

        def callback(args):
            
            positivo_atual = int(args[0][0])
            positivo_atual += 1
            print("positivo atualizado", positivo_atual)

            self.db.update_positivo(lat, lon, positivo_atual)

            msg = "feedback<&>" + 'Vaga joinha'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)

    def negativar_vaga(self,client, lat, lon):

        d = self.db.consulta_negativa(lat,lon)

        def callback(args):
            
            negativo_atual = int(args[0][0])
            negativo_atual += 1
            print("negativo atualizado", negativo_atual)

            self.db.update_negativo(lat, lon, negativo_atual)

            msg = "feedback<&>" + 'Vaga joinha'

            client.sendMessage(msg.encode(encoding='utf_8'))
        
        d.addCallback(callback)
