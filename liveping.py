#! /usr/bin/env python

from scapy.all import *
from time import *
import sys
import netifaces

ipToMac = {"10.0.0.1":"10:10:10:10:10:11","10.0.0.2":"10:10:10:10:10:12",
        "10.0.0.3":"10:10:10:10:10:13","10.0.0.4":"10:10:10:10:10:14"}

def ping(host, iface, port=10022, count=100):
    packet = Ether(dst=ipToMac[host])/IP(dst=host)/TCP(sport=port,dport=port,flags="S")
    for x in range(count):
        t = 0.0
        t1 = time()
        ans, unans = srp(packet, iface=iface, timeout = 15, verbose = 0)
        t2 = time()
        t+=t2-t1
        s = '{} {}\n'.format(x, t*1000)
        sys.stderr.write(s)
        sleep(1)


if __name__=="__main__":
    interfaces = netifaces.interfaces()
    if len(sys.argv) <= 1:
        ping('10.0.0.4', interfaces[1])
    elif len(sys.argv) == 2:
        ping(sys.argv[1], interfaces[1])
    else:
        ping(sys.argv[1], interfaces[1], int(sys.argv[2]))