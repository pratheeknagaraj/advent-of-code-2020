#!/usr/bin/python3

with open('12_input', 'r') as f:
    lines = f.readlines()

directions = [l.strip() for l in lines]

pos = [0,0]
face = (1,0)

faces = [(1,0),(0,-1),(-1,0),(0,1)]

for d in directions:
    m, n = d[0], int(d[1:])
    if m == 'N':
        pos[1] -= n
    elif m == 'S':
        pos[1] += n
    elif m == 'E':
        pos[0] += n
    elif m == 'W':
        pos[0] -= n
    elif m == 'L':
        count = n//90
        ind = faces.index(face)
        new_ind = (ind + count) % 4
        face = faces[new_ind]
    elif m == 'R':
        count = n//90
        ind = faces.index(face)
        new_ind = (ind - count) % 4
        face = faces[new_ind]
    elif m == 'F':
        pos[0] += face[0]*n
        pos[1] += face[1]*n
    #print(pos, face)

def dist(pos):
    return abs(pos[0]) + abs(pos[1])

print(dist(pos))
