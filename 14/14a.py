#!/usr/bin/python3

with open('14_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

mems = {}

mask = 'X'*36

def apply_mask(mask, val):
    new = list(val)
    for i, elem in enumerate(mask):
        if elem != 'X':
            new[i] = elem
    return int(''.join(new), 2)

for line in lines:
    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
    else:
        loc, val = line.split('=')
        loc = loc.split('[')[1].split(']')[0]
        val = str(bin(int(val.strip())))[2:].zfill(36)
        mems[loc] = apply_mask(mask, val)

#print(mems)
print(sum(mems.values()))
