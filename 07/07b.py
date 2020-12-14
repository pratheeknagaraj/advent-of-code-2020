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
            parts = i.split()
            count = int(parts[-4])
            color = ' '.join(parts[-3:-1])
            inner.append((count, color))

    return (outer, inner)

for line in lines:
    outer, inner = get_parts(line)
    bag_map[outer] = inner

#print(bag_map)

start = 'shiny gold'

cache = {}

def recurse(bag):
    if bag in cache:
        return cache[bag]
    inside_bags = bag_map[bag]
    if not inside_bags:
        cache[bag] = 1
        return 1
    total = 1
    for elem in inside_bags:
        total += elem[0] * recurse(elem[1])
    cache[bag] = total
    return total

print(recurse(start) - 1)
#print(cache)

