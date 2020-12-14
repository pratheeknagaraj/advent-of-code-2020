#!/usr/bin/python3

with open('10_input', 'r') as f:
    lines = f.readlines()

nums = [int(l.strip()) for l in lines]

nums = sorted(nums) + [max(nums)+3]

cur = 0
diffs = [0,0,0]

for num in nums:
    diff = num - cur
    cur = num
    diffs[diff-1] += 1

#print(diffs[0])
#print(diffs[2])
print(diffs[0] * diffs[2])
