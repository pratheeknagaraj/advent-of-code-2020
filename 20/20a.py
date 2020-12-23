#!/usr/bin/python3

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

#t = Tile(1, ['AB','CD'], 2)

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

for t in tiles:
    edge_sets = t.edges
    for edge_set in edge_sets:
        for edge in edge_set:
            edge_counter[edge] += 1

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
        #print(t.tile_id)
        corners.append(t)

product = 1
if len(corners) != 4:
    print("Error, can't find the 4 corners")
else:
    for c in corners:
        product *= c.tile_id
print(product)

