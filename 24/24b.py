#!/usr/bin/python3

from collections import defaultdict

with open('24_input', 'r') as f:
    lines = f.readlines()

tiles = [i.strip() for i in lines]

def move(p, d):
    return (p[0]+d[0],p[1]+d[1],p[2]+d[2])

e = (1,-1,0)
w = (-1,1,0)
se = (0,-1,1)
sw = (-1,0,1)
ne = (1,0,-1)
nw = (0,1,-1)

adjs = [e,w,se,sw,ne,nw]

def handle_tile(dirs):
    #print(dirs)
    pos = (0,0,0)

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

states = dict()

for t in tiles:
    end = handle_tile(t)
    if end in states:
        states.pop(end)
    else:
        states[end] = 1

#print(states)

def run_day(states):
    prev = states
    new = dict()

    black_tiles = prev.keys()

    white_new_tiles = defaultdict(int)
    for pos in black_tiles:
        black_adj = 0
        for a in adjs:
            check = move(pos, a)
            if check in prev:
                black_adj += 1
            else:
                white_new_tiles[check] += 1
        if black_adj == 1 or black_adj == 2:
            new[pos] = 1

    for key, val in white_new_tiles.items():
        if val == 2:
            new[key] = 1

    return new

t = 0
count = len(states.values())
#print(f"Day {t}: {count}")

days = 100
for t in range(1, days+1):
    states = run_day(states)
    count = len(states.values())
    #print(f"Day {t}: {count}")

count = len(states.values())
print(count)
