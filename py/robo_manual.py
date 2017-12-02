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

    ppa = Ponto(-22.973870, -43.387209)
    ppb = Ponto(-22.974320, -43.387207)
    ppc = Ponto(-22.974102, -43.387241)
    ppd = Ponto(-22.974095, -43.387001)
    
    ppa.add_vaga(ws)
    ppb.add_vaga(ws)
    ppc.add_vaga(ws)
    ppd.add_vaga(ws)

    for i in range(5):
        ppa.positive(ws)
        ppb.positive(ws)
        ppc.positive(ws)
    
    for i in range(10):
        ppc.negative(ws)
        ppd.negative(ws)

    ppa.add_vaga(ws)
    ppb.add_vaga(ws)
    ppc.add_vaga(ws)
    ppd.add_vaga(ws)

    ppa.add_vaga(ws)
    ppb.add_vaga(ws)
    ppc.add_vaga(ws)
    ppd.add_vaga(ws)


    time.sleep(1)

    ws.send('todas_vagas')

    result =  ws.recv()
    print("Received '%s'" % result)
    #ws.close()



