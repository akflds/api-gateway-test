#!/usr/bin/python3

import requests, json
import time, sched

def monitor(cs, cb):
    maxb = int(cs * 0.9)
    minb = int(cb * 0.8)
    if (cb >= maxb):
        write(True, cs)
    else:
        write(False, cs)

def write(inc, cs):
    if inc:
        nv = int(cs*1.1)

        r = requests.put(url='http://localhost:5000/api/shaperValue/', json={'shaperValue': nv})
    else:
        nv = int(cs*0.8)
        r = requests.put(url='http://localhost:5000/api/shaperValue/', json={'shaperValue': nv})

st=time.time()

while True:
    r = requests.get(url='http://localhost:5000/api/vals/')
    cshaper = r.json()['vals']['shaperValue']
    cbandwidth = r.json()['vals']['bandwidth']
    print(f'Shaper: {cshaper}\tBandwidth: {cbandwidth}')
    monitor(cshaper, cbandwidth)
    time.sleep(5- ((time.time() - st) % 5))
