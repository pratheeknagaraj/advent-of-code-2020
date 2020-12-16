#!/usr/bin/python3

with open('16_input', 'r') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

ranges = lines[:lines.index('')]
my_ticket = lines[lines.index('your ticket:')+1]
nearby_tickets = lines[lines.index('nearby tickets:')+1:]

valid_nums = set()

for l in ranges:
    ranges = l.split(':')[1].strip()
    parts = ranges.split()
    front, back = parts[0], parts[2]
    
    f_i, f_j = front.split('-')
    b_i, b_j = back.split('-')
    f_i, f_j = int(f_i), int(f_j)
    b_i, b_j = int(b_i), int(b_j)

    valid_nums.update(set(range(f_i, f_j+1)))
    valid_nums.update(set(range(b_i, b_j+1)))

invalid_nums = []
for nearby_ticket in nearby_tickets:
    nums = [int(n) for n in nearby_ticket.split(',')]
    for n in nums:
        if n not in valid_nums:
            invalid_nums.append(n)

print(sum(invalid_nums))
