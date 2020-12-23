#!/usr/bin/python3

import copy
import math
import sys

from collections import defaultdict

with open('20_input', 'r') as f:
    data = f.read()

parts = data.split('\n\n')

# Each tile has 8 configurations

# Input Tile
# AB
# CD

# Rotate
# CA DC BD
# DB BA AC

# Flip Horizontal
# BA DB CD AC
# DC CA AB BD

# Flip Vertical (same as above)
# CD AC BA DB
# AB BD DC CA

class Tile:

    def __init__(self, tile_id, tile_data, dim=10):
        self.tile_id = tile_id
        self.tile_data = tile_data
        self.dim = dim

        self.edge()

    def edge(self):
        top = self.tile_data[0]
        bottom = self.tile_data[self.dim-1]
        left = ''.join(i[0] for i in self.tile_data)
        right = ''.join(i[self.dim-1] for i in self.tile_data)

        self.edge = (top, right, bottom, left)

        self.gen_edges()

    def gen_edges(self):
        a, b, c, d = self.edge
        w, x, y, z = a[::-1], b[::-1], c[::-1], d[::-1]
        # a: AB, b: BD, c: CD, d: AC
        # w: BA, x: DB, y: DC, z: CA
        self.edges = [
            (a,b,c,d),
            (z,a,x,c),
            (y,z,w,x),
            (b,y,d,w),
            (w,d,y,b),
            (x,w,z,y),
            (c,x,a,z),
            (d,c,b,a)
        ]
        #print(self.edges)

    def orient(self, perm_id):
        flips = perm_id // 4
        rotates = perm_id % 4

        new_data = flip_horizontal(self.tile_data) if flips else self.tile_data
        for i in range(rotates):
            new_data = rotate_right(new_data, self.dim)
        self.oriented_data = new_data
        self.perm_id = perm_id
        self.block = [r[1:self.dim-1] for r in self.oriented_data[1:self.dim-1]]

    def __str__(self):
        return str(self.tile_id)

    def __repr__(self):
        return self.__str__()

def rotate_right(data, dim):
    new_data = []
    for i in range(dim):
        new_data.append(''.join([r[i] for r in data][::-1]))
    return new_data

def flip_horizontal(data):
    new_data = []
    for d in data:
        new_data.append(d[::-1])
    return new_data

#t = Tile(1, ['AB','CD'], 2)
#for i in range(8):
#    t.orient(i)

tiles = []
def create_tile(data):
    p = data.split('\n')
    tile_id = int(p[0].split()[1][:-1])
    tile_data = [r for r in p[1:] if r]
    return Tile(tile_id, tile_data)

for p in parts:
    t = create_tile(p)
    tiles.append(t)

edge_counter = defaultdict(int)
edge_orientations = defaultdict(list)

for t in tiles:
    edge_sets = t.edges
    for perm_id, edge_set in enumerate(edge_sets):
        for side_id, edge in enumerate(edge_set):
            edge_counter[edge] += 1
            edge_orientations[(edge, side_id)].append((t.tile_id, perm_id, t))

#print([len(i) for i in edge_orientations.values()])

#print(len(tiles))
#print(edge_counter)

corners = []

for t in tiles:
    counts = []
    for e in t.edge:
        count = edge_counter[e]
        counts.append(count)
    t.counts = counts
    if sum(counts) == 24:
        corners.append(t)

grid_dim = int(math.sqrt(len(tiles)))

grid = []
for i in range(grid_dim):
    row = [None]*grid_dim
    grid.append(row)

tile_dim = len(corners[0].tile_data)

selected_tiles = set()

top_left = corners[0]
selected_tiles.add(top_left.tile_id)

#print(f"Top Left ID: {top_left.tile_id}")

for i in range(len(top_left.edges)):
    # Top and Bottom should be unique
    perm = top_left.edges[i]
    if edge_counter[perm[0]] == 4 and edge_counter[perm[3]] == 4:
        top_left.orient(i)
        #print(f"Orientation for top left: {i}")
        break

grid[0][0] = top_left

for i in range(grid_dim):
    for j in range(grid_dim):
        #print(f"Selecting Tile for: ({i}, {j})")
        if grid[i][j] != None:
            continue
        else:
            if i == 0 or j > 0:
                # Match on left
                prev = grid[i][j-1]
                prev_orient = prev.edges[prev.perm_id]
                edge_match = prev_orient[1]
                choices = edge_orientations[(edge_match, 3)]
                selected = choices[0] if choices[0][0] not in selected_tiles else choices[1]
                t_id, t_perm, t = selected
                selected_tiles.add(t_id)
                t.orient(t_perm)
                grid[i][j] = t
            elif j == 0:
                # Match on above
                prev = grid[i-1][j]
                prev_orient = prev.edges[prev.perm_id]
                edge_match = prev_orient[2]
                choices = edge_orientations[(edge_match, 0)]
                selected = choices[0] if choices[0][0] not in selected_tiles else choices[1]
                t_id, t_perm, t = selected
                selected_tiles.add(t_id)
                t.orient(t_perm)
                grid[i][j] = t
            else:
                print("Do not reach here")
                sys.exit(1)

#print(grid)

image = []
red_tile_dim = tile_dim - 2
im_size = grid_dim * red_tile_dim
for x in range(im_size):
    row = [None] * im_size
    image.append(row)

for i in range(grid_dim):
    for j in range(grid_dim):
        tile = grid[i][j]
        data = tile.block
        for x in range(red_tile_dim):
            for y in range(red_tile_dim):
                a = i * red_tile_dim + x
                b = j * red_tile_dim + y
                image[a][b] = data[x][y]

def print_image(image):
    im_size = len(image)
    for i in range(im_size):
        print(''.join(image[i]))

# Sea Monster
"""
                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""
monster = [
    (0,18),
    (1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),
    (2,1),(2,4),(2,7),(2,10),(2,13),(2,16)
]

def find_monsters(image):
    search_image = copy.deepcopy(image)
    dim = len(image)
    monster_count = 0
    for i in range(dim):
        for j in range(dim):
            found = True
            for m in monster:
                x, y = i+m[0], j+m[1]
                if x >= dim or y >= dim or search_image[x][y] != '#':
                    found = False
                    break
            if found:
                for m in monster:
                    x, y = i+m[0], j+m[1]
                    #print(search_image)
                    search_image[x][y] = 'O'
                monster_count += 1
    return search_image, monster_count

final_image = None
for i in range(8):
    flips = i // 4
    rotates = i % 4
    #print(f"Searching orientation with: {flips} flips and {rotates} rotations")

    new_image = flip_horizontal(image) if flips else image
    for i in range(rotates):
        new_image = rotate_right(new_image, im_size)

    if flips or rotates:
        new_image = [list(r) for r in new_image]
    found_image, count = find_monsters(new_image)
    if count > 0:
        #print(f"Monster count: {count}")
        #print_image(found_image)
        final_image = found_image
        break

if not final_image:
    print("Failed to find monsters")
    sys.exit(1)

roughness = 0
for row in final_image:
    roughness += row.count('#')

print(roughness)
