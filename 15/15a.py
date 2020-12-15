#!/usr/bin/python3

with open('15_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

def solve(nums):
    last_seen = {}
    turn = 1

    for num in nums[:-1]:
        last_seen[num] = turn
        turn += 1
    turn += 1

    last_num = nums[-1]

    for t in range(turn, 2020):
        if last_num in last_seen:
            diff = t - last_seen[last_num] - 1
            last_seen[last_num] = t - 1
            last_num = diff
        else:
            last_seen[last_num] = t - 1
            last_num = 0
        #print(f"Turn: {t}, Value: {last_num} ")

    t += 1
    val = 0
    if last_num in last_seen:
        val = t - last_seen[last_num] - 1
    #print(f"Turn: {t}, Value: {val} ")
    return val

for line in lines:
    nums = [int(l) for l in line.split(',')]
    print(solve(nums))
