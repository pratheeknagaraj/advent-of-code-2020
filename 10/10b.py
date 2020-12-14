#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

nums = [int(l.strip()) for l in lines]

nums = sorted(nums) + [max(nums)+3]

nums_set = set(nums)

cache = {}

cache[max(nums)] = 1

def recurse(num):
    if num in cache:
        return cache[num]

    total = 0
    for i in (1,2,3):
        new = num + i
        if new in nums_set:
            total += recurse(new)
    
    cache[num] = total
    return total

start = 0

print(recurse(start))
