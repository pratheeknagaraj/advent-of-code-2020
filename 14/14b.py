#!/usr/bin/python3

import sys

with open('14_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

mems = {}

BITS = 36

mask = 'X'*BITS

def apply_mask(mask, val):
    new = list(val)
    for i, elem in enumerate(mask):
        if elem == '0':
            pass
        elif elem == '1':
            new[i] = '1' 
        elif elem == 'X':
            new[i] = 'X'
    return new

def get_matches(masked):
    nums = [0]

    MAX_SIZE = 2**10

    for i, elem in enumerate(masked):
        bit_val = 2**(BITS-i-1)
        if elem == '0':
            pass
        elif elem == '1':
            nums = [n + bit_val for n in nums]
        elif elem == 'X':
            nums = nums + [n + bit_val for n in nums]
    
        if len(nums) >= MAX_SIZE:
            print("Too many addresses, exiting")
            sys.exit(1)

    return nums

for line in lines:
    if line.startswith('mask'):
        mask = line.split('=')[1].strip()
    else:
        loc, val = line.split('=')
        loc = loc.split('[')[1].split(']')[0]
        val = int(val.strip())

        addr = str(bin(int(loc)))[2:].zfill(36)
        masked = apply_mask(mask, addr)
        addrs = get_matches(masked)

        for a in addrs:
            mems[a] = val

#print(mems)
print(sum(mems.values()))
