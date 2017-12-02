#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from autobahn.twisted.resource import WebSocketResource
from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

from factory import Factory
from protocol import Protocol

if __name__ == "__main__":
    log.startLogging(sys.stdout)

    port = 40000

    server_address = "ws://127.0.0.1:" + str(port)

    factory = Factory(server_address)
    factory.protocol = Protocol
    resource = WebSocketResource(factory)

    reactor.listenTCP(port, factory)

    reactor.run()
