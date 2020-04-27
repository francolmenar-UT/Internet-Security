import csv

csvfile = open('out.csv')
reader = csv.DictReader(csvfile)

flows = []

for row in reader:
    flows.append(row)

print('Flow records count:', len(flows))

average_duration = 0
average_packets = 0
average_bytes = 0

for flow in flows:
    average_duration += float(flow['duration'])
    average_packets += int(flow['pkt'])
    average_bytes += int(flow['oct'])

average_traffic = average_bytes / average_duration

average_duration /= len(flows)
average_packets /= len(flows)
average_bytes /= len(flows)

print('Average flow record duration:', average_duration)

print('Average number of packets per flow:', average_packets)

print('Average number of bytes per flow:', average_bytes)

print('Average traffic rate per flow:', average_traffic)

ip = '128.160.78.76'
bmax = 0
for flow in flows:
    if flow['sip'] == ip:
        traffic = int(flow['oct']) / float(flow['duration'])
        bmax = max(traffic, bmax)
print('Traffic peak for ip', ip, ':', bmax)

ip = '128.170.241.107'
bmax = 0
for flow in flows:
    if flow['sip'] == ip:
        traffic = int(flow['oct']) / float(flow['duration'])
        bmax = max(traffic, bmax)
print('Traffic peak for ip', ip, ':', bmax)
