#from websocket import create_connection

import websocket
import time

atraso = 0.2

class Ponto(object):
    def __init__(self, la, lo):
        self.la = la
        self.lo = lo

    def add_vaga(self,W):
        W.send('add_vaga<&>{};{}'.format(self.la,self.lo))
        time.sleep(atraso)
    
    def positive(self,W):
        time.sleep(atraso)
        W.send('positivar_vaga<&>{};{}'.format(self.la,self.lo))
    
    def negative(self,W):
        time.sleep(atraso)
        W.send('negativar_vaga<&>{};{}'.format(self.la,self.lo))


if __name__ == "__main__":

    ws = websocket.create_connection("ws://localhost:40000")

    ppV1 = Ponto(-22.893999, -43.295744)
    ppV2 = Ponto(-22.893706, -43.296856)
    ppV3 = Ponto(-22.896001, -43.296213)
    ppV4 = Ponto(-22.896844, -43.293645)
    ppV5 = Ponto(-22.895162, -43.289742)
    ppV6 = Ponto(-22.894117, -43.290065)
    ppV7 = Ponto(-22.893256, -43.289415)
    ppV8 = Ponto(-22.893114, -43.289307)
    ppV9 = Ponto(-22.890849, -43.293706)

    ppV1.add_vaga(ws)
    ppV2.add_vaga(ws)
    ppV3.add_vaga(ws)
    ppV4.add_vaga(ws)
    ppV5.add_vaga(ws)
    ppV6.add_vaga(ws)
    ppV7.add_vaga(ws)
    ppV8.add_vaga(ws)
    ppV9.add_vaga(ws)


    for i in range(5):
        ppV1.positive(ws)
        ppV2.positive(ws)
        ppV3.positive(ws)
    
    for i in range(10):
        ppV3.negative(ws)
        ppV4.negative(ws)
        ppV5.negative(ws)


    time.sleep(1)

    #ws.send('todas_vagas')

    #result =  ws.recv()
    #print("Received '%s'" % result)
    #ws.close()

