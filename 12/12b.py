#!/usr/bin/python3

with open('12_input', 'r') as f:
    lines = f.readlines()

directions = [l.strip() for l in lines]

pos = [0,0]
waypoint = [10,-1]

def rotate_clockwise(i):
    o = [-i[1], i[0]]
    return o

def rotate_counterclockwise(i):
    o = [i[1], -i[0]]
    return o

for d in directions:
    m, n = d[0], int(d[1:])
    if m == 'N':
        waypoint[1] -= n
    elif m == 'S':
        waypoint[1] += n
    elif m == 'E':
        waypoint[0] += n
    elif m == 'W':
        waypoint[0] -= n
    elif m == 'L':
        count = n//90
        for i in range(count):
            waypoint = rotate_counterclockwise(waypoint)
    elif m == 'R':
        count = n//90
        for i in range(count):
            waypoint = rotate_clockwise(waypoint)
    elif m == 'F':
        pos[0] += waypoint[0]*n
        pos[1] += waypoint[1]*n
    #print(pos, waypoint)

def dist(pos):
    return abs(pos[0]) + abs(pos[1])

print(dist(pos))
