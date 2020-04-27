# Parameters
interface = "eth0"  # Interface you want to use

source = "10.0.0.3"  # spoofed source IP address
destination = "10.0.0.2"  # destination IP address
s_port = 58678  # source port
d_port = 53  # destination port

time_to_live = 128  # IP TTL
query_name = "loudly-purple-send.security.utwente.nl."  # DNS Query Name

query_type = ["ANY", "A", "AAAA", "CNAME", "MX", "NS", "PTR", "CERT", "SRV", "TXT", "SOA"]  # DNS Query Types
