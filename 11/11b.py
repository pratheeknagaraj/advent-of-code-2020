#!/usr/bin/python3

import copy

with open('11_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

grid = []
for row in lines:
    new_row = []
    for elem in row:
        new_row.append(None if elem == '.' else 0)
    grid.append(new_row)

def sim(grid):
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    new_grid = copy.deepcopy(grid)

    len_x, len_y = len(grid), len(grid[0])

    for i in range(len_x):
        for j in range(len_y):
            if grid[i][j] == None:
                new_grid[i][j] = None

            elif grid[i][j] == 0:
                new_grid[i][j] = 1
                exit = False
                for d in dirs:
                    x, y = i, j
                    found = False
                    while not found:
                        x, y = x + d[0], y + d[1]
                        if 0 <= x < len_x and 0 <= y < len_y:
                            if grid[x][y] == 1:
                                new_grid[i][j] = 0
                                exit = True
                                found = True
                                break
                            elif grid[x][y] == 0:
                                found = True
                                break
                        else:
                            found = True
                            break
                    if exit:
                        break

            elif grid[i][j] == 1:
                new_grid[i][j] = 1
                count = 0
                exit = False
                for d in dirs:
                    x, y = i, j
                    found = False
                    while not found:
                        x, y = x + d[0], y + d[1]
                        if 0 <= x < len_x and 0 <= y < len_y:
                            if grid[x][y] == 1:
                                count += 1
                                if count >= 5:
                                    new_grid[i][j] = 0
                                    exit = True
                                    found = True
                                    break
                                found = True
                                break
                            elif grid[x][y] == 0:
                                found = True
                                break
                        else:
                            found = True
                            break
                    if exit:
                        break


    return new_grid

def same(g_a, g_b):
    t_a = tuple(tuple(r_a) for r_a in g_a)
    t_b = tuple(tuple(r_b) for r_b in g_b)
    if t_a == t_b:
        return True
    return False

def count(grid):
    total = sum(sum(filter(None, r)) for r in grid)
    return total

def print_grid(grid):
    for r in grid:
        s = ''
        for e in r:
            if e == None:
                s += '.'
            elif e == 0:
                s += 'L'
            else:
                s += '#'
        print(s)

max_iter = 1000
for i in range(max_iter):
    #print(f"Iteration: {i}")
    new_grid = sim(grid)
    #print_grid(new_grid)
    if same(grid, new_grid):
        print(count(new_grid))
        break
    grid = new_grid
