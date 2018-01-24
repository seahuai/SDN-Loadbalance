#!/usr/bin/python
# -*- coding: utf-8 -*-
# 负载均衡

# sudo mn --custom ldTopo.py --topo topo --controller=remote,ip=127.0.0.1,port=6633

from mininet.topo import Topo

class LDTopo(Topo):

    def __init__(self):
        Topo.__init__(self)

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s2, h3)
        self.addLink(s2, s3)
        self.addLink(s2, s1)
        self.addLink(s3, s1)


topos = {"topo": (lambda : LDTopo()) }

