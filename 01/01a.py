#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

nums = [int(n.strip()) for n in lines]

nums_set = set(nums)

for num in nums:
    rem = 2020 - num
    if rem in nums_set:
        print(num, rem)
        print(num * rem)
        break
