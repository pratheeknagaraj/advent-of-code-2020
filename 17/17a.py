#!/usr/bin/python3

import copy

with open('17_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

n = len(lines[0].strip())

cycles = 6
init_n = n + 2 * cycles

grid = []
for i in range(init_n):
    plane = []
    for j in range(init_n):
        row = []
        for k in range(init_n):
            row.append(0)
        plane.append(row)
    grid.append(plane)

init_states = []
for l in lines:
    row = [0 if i == '.' else 1 for i in list(l.strip())]
    init_states.append(row)

#print(init_states)

for i in range(n):
    for j in range(n):
        grid[cycles+n//2][cycles+i][cycles+j] = init_states[i][j]

def sim(grid):
    new_grid = copy.deepcopy(grid)
    
    dirs = [(i,j,k) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2)]
    dirs.remove((0,0,0))

    m = len(grid)

    def count_active(cell, dirs):
        i, j, k = cell
        count = 0
        for d in dirs:
            x, y, z = i+d[0], j+d[1], k+d[2]
            if 0 <= x < m and 0 <= y < m and 0 <= z < m:
                count += grid[x][y][z]
        return count

    for i in range(m):
        for j in range(m):
            for k in range(m):
                count = count_active((i,j,k), dirs)
                cur = grid[i][j][k]
                if cur == 0:
                    new_grid[i][j][k] = 1 if count == 3 else 0
                else:
                    new_grid[i][j][k] = 1 if count in (2,3) else 0

    return new_grid

for i in range(cycles):
    grid = sim(grid)

total_count = 0

for i in range(init_n):
    for j in range(init_n):
        for k in range(init_n):
            total_count += grid[i][j][k]

#print(grid)
print(total_count)
