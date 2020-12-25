#!/usr/bin/python3

import copy

from collections import defaultdict

with open('24_input', 'r') as f:
    lines = f.readlines()

tiles = [i.strip() for i in lines]

def move(p, d):
    return (p[0]+d[0],p[1]+d[1],p[2]+d[2])

def handle_tile(dirs):
    #print(dirs)
    pos = (0,0,0)

    e = (1,-1,0)
    w = (-1,1,0)
    se = (0,-1,1)
    sw = (-1,0,1)
    ne = (1,0,-1)
    nw = (0,1,-1)

    while dirs:
        if dirs.startswith('e'):
            pos = move(pos, e)
            dirs = dirs[1:]
        elif dirs.startswith('w'):
            pos = move(pos, w)
            dirs = dirs[1:]
        elif dirs.startswith('se'):
            pos = move(pos, se)
            dirs = dirs[2:]
        elif dirs.startswith('sw'):
            pos = move(pos, sw)
            dirs = dirs[2:]
        elif dirs.startswith('ne'):
            pos = move(pos, ne)
            dirs = dirs[2:]
        elif dirs.startswith('nw'):
            pos = move(pos, nw)
            dirs = dirs[2:]

    return pos

states = defaultdict(int)

for t in tiles:
    end = handle_tile(t)
    states[end] += 1

#print(states)
total = sum([v % 2 for v in states.values()])
print(total)
