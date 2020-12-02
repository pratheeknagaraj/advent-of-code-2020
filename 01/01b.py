#!/usr/bin/python3

with open('01_input', 'r') as f:
    lines = f.readlines()

nums = [int(n.strip()) for n in lines]

nums = sorted(nums)

nums_dict = dict()

target = 2020

for i, num1 in enumerate(nums):
    for num2 in nums[i+1:]:
        if num1 + num2 > target:
            break
        tot = num1 + num2
        # There will be only one solution, so if an key, val exists it can be replaced
        nums_dict[num1 + num2] = (num1, num2)

for num in nums:
    rem = 2020 - num
    if rem in nums_dict:
        val = nums_dict[rem]
        print(num, val[0], val[1])
        print(num * val[0] * val[1])
        break
