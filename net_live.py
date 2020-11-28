from netaddr import *
import subprocess
import pprint
import copy

nets = [
    "192.168.1.0/25",
    "192.168.1.128/25"
]

servers = [
    "192.168.1.1",
    "192.168.1.3"
]

obj = {}

sub = {
    "tot": 0,
    "up": 0,
    "down": 0,
    "ip_list": [],
    "SAG Servers": [],
    "SE Servers": [],
}


for net in nets:
    n = IPNetwork(net)
    obj[net] = copy.deepcopy(sub)
    print(f"process {net}")
    # for i in range(0, n.size):
    for i in range(0, 10):
        ip = str(n[i])
        obj[net]["tot"] += 1
        canPing = subprocess.call(f"ping /n 1 /w 100 {ip}",
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)
        if canPing == 0:
            print('I can ping %s' % ip)
            obj[net]["up"] += 1
            obj[net]["ip_list"].append(ip)
            if ip in servers:
                obj[net]["SAG Servers"].append(ip)
            else:
                obj[net]["SE Servers"].append(ip)
        if canPing == 1:
            print('%s is not responding' % ip)
            obj[net]["down"] += 1


pprint.pprint(obj)
