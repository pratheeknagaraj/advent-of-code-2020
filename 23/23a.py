#!/usr/bin/python3

import copy

with open('23_input', 'r') as f:
    data = f.read()

cups = [int(i) for i in list(data.strip())]

def move(cur, cups):
    #print(cups)
    sel = cups[cur]
    #print(sel)
    new = cups.copy()
    remove = 3
    removed = []
    while remove > 0:
        if cur+1 >= len(new):
            ind = 0
        else:
            ind = (cur+1) % len(new)
        removed.append(new.pop(ind))
        remove -= 1
    #print(removed)
    dest = sel-1
    while True:
        if dest == 0:
            dest = 9
        if dest not in new:
            dest -= 1
        else:
            pos = new.index(dest)
            new = new[:pos+1] + removed + new[pos+1:]
            break
    #print(dest)
    ind_sel = new.index(sel)
    new_cur = (ind_sel+1) % len(new)
    return new, new_cur

move_count = 100
cur = 0
for i in range(1, move_count+1):
    #print(f"Move: {i}")
    cups, cur = move(cur, cups)
    #print()

#print(cups)

while cups[0] != 1:
    cups.append(cups.pop(0))

print(''.join(str(i) for i in cups[1:]))
