#!/usr/bin/python3

with open('03_input', 'r') as f:
    lines = f.readlines()

rows = [r.strip() for r in lines]

width = len(rows[0])
height = len(rows)

steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]

val = 1

for step in steps:

    counter = 0
    pos = (0,0)

    #print(step)

    for i, row in enumerate(rows[step[1]::step[1]]):
        pos = ((pos[0] + step[0]) % width, pos[1] + step[1])
        if row[pos[0]] == '#':
            counter += 1
        #print(pos, row[pos[0]])

    #print(counter)

    val *= counter

print(val)
