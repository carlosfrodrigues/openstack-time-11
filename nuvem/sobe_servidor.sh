#!/usr/bin/env bash

# para logar na maquina
# chave publica criada no horizon: #chave = time11famaral.pem
# ssh -i time11famaral.pem ubuntu@10.20.3.197

# para mover aruivos
# scp -C -i #chave #arquivo ubuntu@10.20.3.197:/home/ubuntu/#PASTA/

sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf

sudo apt-get -y update

sudo apt-get -y install unzip

sudo apt-get -y install gcc

sudo apt-get -y install python3-setuptools
sudo apt-get -y install python3-dev

sudo easy_install3 pip

sudo pip install autobahn
sudo pip install websockets
sudo pip install websocket-client
sudo pip install Twisted

mkdir /tmp/vagaAZUL

#python3 py/main.py