#!/usr/bin/python3

with open('09_input', 'r') as f:
    lines = f.readlines()

nums = [int(l.strip()) for l in lines]

preamble_size = 25

sum_cache = dict()
table = []

for i in range(preamble_size):
    row = []
    front = nums[i]
    for j in range(i+1, preamble_size):
        val = front + nums[j]
        sum_cache[val] = sum_cache.get(val, 0) + 1
        row.append(front + nums[j])
    table.append((front, row))

#print(table)
#print(sum_cache)

pointer = preamble_size

while pointer < len(nums):
    cur = nums[pointer]
    if cur not in sum_cache:
        print(cur)
        break
    else:
        old = nums[pointer-preamble_size]
        for elem in table[0][1]:
            s = sum_cache[elem]
            if s == 1:
                del sum_cache[elem]
            else:
                sum_cache[elem] -= 1
        table = table[1:]
        for i in range(preamble_size-1):
            new_val = table[i][0] + cur
            table[i][1].append(new_val)
            sum_cache[new_val] = sum_cache.get(new_val, 0) + 1
        table.append((cur,[]))

    pointer += 1
    #print(pointer, table, sum_cache)

