#!/usr/bin/python3

with open('07_input', 'r') as f:
    lines = f.readlines()

bag_map = {}

def get_parts(line):
    front, back = line.split('contain')
    outer = ' '.join(front.split()[:2])

    inner = []
    if 'no other' not in back:
        for i in back.split(','):
            color = ' '.join(i.split()[-3:-1])
            inner.append(color)

    return (outer, inner)

for line in lines:
    outer, inner = get_parts(line)
    for elem in inner:
        if elem not in bag_map:
            bag_map[elem] = set()
        bag_map[elem].add(outer)

#print(bag_map)

start = 'shiny gold'

containers = set()

search_list = list(bag_map[start])

while search_list:
    cur = search_list.pop()
    if cur not in containers:
        containers.add(cur)
        for elem in bag_map.get(cur, []):
            if elem not in containers:
                search_list.append(elem)

#print(containers)
print(len(containers))
