from kamene.all import *
from tqdm import tqdm

filename = 'team4.pcap'

SRC_IP = '192.168.203.64'
DST_IP = '192.168.22.252'
SRC_PORT = 443
DST_PORT = 50670

TTL_LOW = 54
TTL_HIGH = 64

reader = PcapReader(filename)

secret_bit_string = ""

pkt_count = 0

pkt_num = 0

for pkt in tqdm(reader):
    pkt_num += 1

    # If payload is not tcp skip
    if pkt.payload.payload.aliastypes != [kamene.layers.inet.IP]:
        continue
    
    ip = pkt.payload.payload

    # Check source and destination IPs    
    if ip.src != SRC_IP or ip.dst != DST_IP:
        continue
    
    # If payload is not tcp skip
    if ip.payload.aliastypes != [kamene.layers.inet.TCP]:
        continue

    # Check source and destination ports
    if ip.payload.sport != SRC_PORT or ip.payload.dport != DST_PORT:
        continue

    # Check that tcp payload is SSL
    
    pkt_count += 1

    print("No:", pkt_num)

    if ip.ttl == TTL_LOW:
        secret_bit_string += "0"
        print("0")
    elif ip.ttl == TTL_HIGH:
        secret_bit_string += "1"
        print("1")
    else:
        print("#")

print("pkt count:", pkt_count)

if len(secret_bit_string) % 8 != 0:
    print("Not %8 bits, probably there was an error")

print("Bit string:", secret_bit_string)

secret = ""
reverse_secret = ""

for i in range (0, int(len(secret_bit_string)/8)):
    sub_str = secret_bit_string[i*8:i*8+8]

    secret += chr(int(sub_str, 2))
    reverse_secret += chr(int(sub_str[::-1], 2))

#print("Secret:", secret)
#print("Reverse:", reverse_secret)

