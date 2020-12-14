#!/usr/bin/python3

with open('09_input', 'r') as f:
    lines = f.readlines()

nums = [int(l.strip()) for l in lines]

target = 23278925
#target = 127

for i in range(len(nums)):
    s = nums[i]
    for j in range(i+1, len(nums)):
        s += nums[j]
        if s > target:
            break
        if s == target:
            #print(min(nums[i:j+1]))
            #print(max(nums[i:j+1]))
            print(min(nums[i:j+1]) + max(nums[i:j+1]))
            break
    if s == target:
        break
