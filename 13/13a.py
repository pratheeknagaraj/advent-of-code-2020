#!/usr/bin/python3

with open('13_input', 'r') as f:
    lines = f.readlines()

earliest = int(lines[0].strip())
busses = lines[1]

bus_list = busses.split(',')
bus_ids = [int(i) for i in bus_list if i.isnumeric()]

bus_ids = sorted(bus_ids)

def wait(e, i):
    return (i - e % i) % i

waits = sorted([(wait(earliest, i), i) for i in bus_ids])

#print(waits[0])
print(waits[0][0] * waits[0][1])
